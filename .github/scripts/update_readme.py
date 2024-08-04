import os
import sys

# Add the parent directory of 'scripts' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from github import Github
from loguru import logger
from config import get_settings
from services.llm_service import LLMService

def main():
    logger.info("README更新プロセスを開始します。")
    
    settings = get_settings()
    llm_service = LLMService()
    g = Github(settings.YOUR_PERSONAL_ACCESS_TOKEN_IRIS)
    repo = g.get_repo(settings.GITHUB_REPOSITORY)

    # 最新のリリースを取得
    latest_release = repo.get_latest_release()
    logger.info(f"最新のリリース: {latest_release.title}")

    # READMEの内容を取得
    readme = repo.get_contents("README.md")
    readme_content = readme.decoded_content.decode("utf-8")

    # LLMにプロンプトを送信
    prompt = f"""
以下の情報を元に、READMEを更新してください：

最新のリリースノート:
{latest_release.body}

現在のREADME:
{readme_content}

更新のガイドライン:
1. 最新の機能や変更点を反映させてください。
2. 既存の構造を維持しつつ、必要な箇所のみを更新してください。
3. リリースノートの詳細すべてをREADMEに含める必要はありません。重要なポイントのみを簡潔に記載してください。
4. バージョン番号や日付を更新してください。

更新されたREADMEの全文を出力してください。
    """

    logger.info("LLMに更新を依頼しています...")
    logger.info(f"プロンプト：\n{prompt}")
    updated_readme = llm_service.get_response(prompt)

    # 更新されたREADMEの内容をファイルに書き込む
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(updated_readme)

    logger.info("READMEの更新が完了しました。")

if __name__ == "__main__":
    main()
