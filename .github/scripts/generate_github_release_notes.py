# .github/scripts/generate_github_release_notes.py

import os
import sys

# Add the parent directory of 'scripts' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger
from config import get_settings
from services.llm_service import LLMService
from services.github_service import GitHubService

def main():
    logger.info("GitHub リリースノート生成プロセスを開始します。")
    
    settings = get_settings()
    llm_service = LLMService()
    github_service = GitHubService()

    # 環境変数から差分とREADMEの内容を取得
    diff = os.getenv('DIFF', '')
    readme = os.getenv('README', '')
    latest_tag = os.getenv('LATEST_TAG', '')

    if not latest_tag:
        logger.error("環境変数 'LATEST_TAG' が設定されていません。")
        sys.exit(1)

    prompt = f"""
以下は、GitHubリポジトリの最新のタグと1つ前のタグの間の差分と、READMEの内容です。
これらの情報を基に、以下の点に注意してリリースノートを生成してください：

1. 主要な変更点を簡潔に要約する
2. 新機能、バグ修正、パフォーマンス改善などをカテゴリ分けして列挙する
3. 破壊的変更がある場合は特に強調する
4. コントリビューターへの謝辞を含める
5. 必要に応じて、アップグレード手順や注意事項を記載する

差分:
{diff}

README:
{readme}

リリースノートを Markdown 形式で生成してください。
    """

    logger.info("LLMを使用してリリースノートを生成します。")
    release_notes = llm_service.get_response(prompt)
    logger.info("リリースノートの生成が完了しました。")

    # GitHubリリースを作成
    try:
        github_service.create_release(latest_tag, release_notes)
        logger.info(f"GitHubリリース {latest_tag} を作成しました。")
    except Exception as e:
        logger.error(f"GitHubリリースの作成中にエラーが発生しました: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
