import os
from typing import List, Dict, Any
from litellm import completion
from github import Github
from enum import Enum

class LLMModel(Enum):
    # GEMINI = "gemini/gemini-pro"
    # GPT4 = "gpt-4o"
    # CLAUDE = "anthropic/claude-2"
    MODEL_NAME = "gemini/gemini-1.5-pro-latest"

class LLMIntegration:
    def __init__(self):
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_repo = os.getenv("GITHUB_REPOSITORY")
        self.issue_number = int(os.getenv("ISSUE_NUMBER", 0))
        self.setup_api_keys()

    def setup_api_keys(self):
        """異なるLLMプロバイダーのAPIキーを設定する"""
        os.environ['GEMINI_API_KEY'] = os.getenv("GEMINI_API_KEY", "")
        os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY", "")
        os.environ['ANTHROPIC_API_KEY'] = os.getenv("ANTHROPIC_API_KEY", "")

    def get_llm_response(self, model: LLMModel, messages: List[Dict[str, str]]) -> str:
        """指定されたLLMモデルからレスポンスを取得する"""
        try:
            response = completion(model=model.value, messages=messages)
            return response['choices'][0]['message']['content']
        except Exception as e:
            print(f"{model.value}からのレスポンス取得中にエラーが発生しました: {str(e)}")
            return ""

    def analyze_github_issue(self) -> List[str]:
        """GitHubイシューを分析し、ラベルを提案する"""
        g = Github(self.github_token)
        repo = g.get_repo(self.github_repo)
        issue = repo.get_issue(number=self.issue_number)

        issue_content = f"タイトル: {issue.title}\n\n本文: {issue.body}"
        prompt = self.create_label_prompt(issue_content)

        response = self.get_llm_response(LLMModel.MODEL_NAME, [
            {"role": "system", "content": "あなたはGitHubイシューを分析し、適切なラベルを提案する助手です。"},
            {"role": "user", "content": prompt}
        ])

        return response.strip().split(', ')

    @staticmethod
    def create_label_prompt(issue_content: str) -> str:
        """ラベル提案用のプロンプトを作成する"""
        return f"""
        以下のGitHubイシューを分析し、次のカテゴリから最大3つの適切なラベルを提案してください：
        - bug: バグ報告
        - feature: 新機能リクエスト
        - enhancement: 既存機能の改善
        - documentation: ドキュメントの改善や追加
        - question: 質問
        - help wanted: 協力が必要
        - good first issue: 初心者向けの課題

        イシューの内容:
        {issue_content}

        回答は以下の形式で提供してください：
        label1, label2, label3
        """

    def apply_labels_and_comment(self, labels: List[str]):
        """提案されたラベルをイシューに適用し、コメントを追加する"""
        g = Github(self.github_token)
        repo = g.get_repo(self.github_repo)
        issue = repo.get_issue(number=self.issue_number)

        applied_labels = []
        for label in labels:
            try:
                issue.add_to_labels(label)
                applied_labels.append(label)
                print(f"ラベル '{label}' が正常に追加されました。")
            except Exception as e:
                print(f"ラベル '{label}' の追加に失敗しました: {str(e)}")

        comment = f"I.R.I.S Bot🤖が以下のラベルを提案し、適用しました：\n\n" + "\n".join([f"- {label}" for label in applied_labels])
        issue.create_comment(comment)
        print("イシューの分析とラベリングが完了し、コメントが追加されました。")

def main():
    llm_integration = LLMIntegration()
    suggested_labels = llm_integration.analyze_github_issue()
    llm_integration.apply_labels_and_comment(suggested_labels)

if __name__ == "__main__":
    main()