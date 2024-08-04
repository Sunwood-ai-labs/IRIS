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
以下は、GitHubリポジトリの最新のタグと1つ前のタグの間の差分と、リポジトリのREADMEの内容です。
これらの情報を基に、以下のテンプレートに従ってリリースノートを生成してください。
生成されたリリースノートは、そのままGitHubのリリースページに掲載されます。

重要な注意事項：
1. リリースノートは主に差分の内容に基づいて生成してください。
2. READMEはプロジェクトの背景情報として参照し、変更内容の文脈を理解するために使用してください。
3. READMEの内容自体を変更点としてリリースノートに含めないでください。
4. 差分に明示されていない変更は、リリースノートに含めないでください。

---

# 差分:
{diff}

---

# リポジトリのREADME（参考情報）:
{readme}

---

# テンプレート:

## 🌟 主な変更点

ここに、このリリースの主要な変更点や新機能を3〜5行で簡潔に要約してください。差分の内容のみを反映させてください。

## ✨ 新機能

- 【重要度: 高】新機能1の簡潔な説明（差分に基づく）
- 【重要度: 中】新機能2の簡潔な説明（差分に基づく）
- 【重要度: 低】新機能3の簡潔な説明（差分に基づく）

## 🐛 バグ修正

- 修正されたバグ1の簡潔な説明（差分に基づく）
- 修正されたバグ2の簡潔な説明（差分に基づく）

## 🚀 パフォーマンス改善

- パフォーマンス改善1の簡潔な説明とその影響（差分に基づく）
- パフォーマンス改善2の簡潔な説明とその影響（差分に基づく）

## 💥 破壊的変更

- **[要注意]** 破壊的変更1の詳細な説明と対応方法（差分に基づく）
- **[要注意]** 破壊的変更2の詳細な説明と対応方法（差分に基づく）

## 📚 ドキュメント更新

- 更新されたドキュメント1の簡潔な説明（差分に基づく）
- 更新されたドキュメント2の簡潔な説明（差分に基づく）

## 🛠 その他の変更

- その他の小さな変更や改善点をリストアップ（差分に基づく）

## 🆙 アップグレード手順

必要な場合のみ、差分に基づいてアップグレード手順を記載してください。

## 📝 注意事項

差分に基づいて、特別な注意が必要な項目がある場合にのみ記載してください。

---

上記のテンプレートに基づいて、差分の内容のみを反映したリリースノートを生成してください。
各セクションの内容は、提供された差分情報に基づいて適切に調整してください。
重要でないセクションは省略しても構いません。
READMEは背景情報としてのみ使用し、その内容自体を変更点として扱わないでください。
出力にはmarkdownのコードブロックを使用せず、そのまま出力してください。
    """

    logger.info("LLMを使用してリリースノートを生成します。")
    logger.debug(f"リリースノート生成プロンプト\n{prompt}")
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
