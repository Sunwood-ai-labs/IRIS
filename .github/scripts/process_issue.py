import os
import openai
from github import Github

# GitHub APIクライアントの初期化
g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPOSITORY"))
issue = repo.get_issue(number=int(os.getenv("ISSUE_NUMBER")))

# OpenAI APIクライアントの初期化
openai.api_key = os.getenv("OPENAI_API_KEY")

# イシューの内容を取得
issue_content = f"Title: {issue.title}\n\nBody: {issue.body}"

# ラベル提案のためのプロンプト
prompt = f"""
以下はGitHubイシューの内容です。この内容を分析し、適切なラベルを提案してください。
ラベルは以下のカテゴリから選択し、最大3つまで提案してください：

- bug: バグ報告
- feature: 新機能リクエスト
- enhancement: 既存機能の改善
- documentation: ドキュメントの改善や追加
- question: 質問
- help wanted: 協力が必要
- good first issue: 初心者向けの課題

イシューの内容：
{issue_content}

回答は以下の形式で提供してください：
label1, label2, label3
"""

# gpt-4oを使用してイシューを分析
response = openai.ChatCompletion.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "You are a helpful assistant that analyzes GitHub issues and suggests appropriate labels."},
    {"role": "user", "content": prompt}
  ],
  max_tokens=50
)

# 提案されたラベルを取得
suggested_labels = response.choices[0].message['content'].strip().split(', ')

# イシューにラベルを適用
for label in suggested_labels:
    try:
        issue.add_to_labels(label)
        print(f"ラベル '{label}' を追加しました。")
    except:
        print(f"ラベル '{label}' の追加に失敗しました。")

# ラベル追加の通知コメントを作成
comment = f"I.R.I.Sが以下のラベルを提案し、適用しました：\n\n" + "\n".join([f"- {label}" for label in suggested_labels])
issue.create_comment(comment)

print("イシューの分析とラベリングが完了し、コメントが追加されました。")