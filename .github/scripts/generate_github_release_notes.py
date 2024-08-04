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
以下は、GitHubリポジトリの最新のタグと1つ前のタグの間の差分と、以前のリポジトリのREADMEの内容です。
これらの情報を基に、以下のテンプレートに従ってリリースノートを生成してください。
生成されたリリースノートは、そのままGitHubのリリースページに掲載されます。
出力にはmarkdownのコードブロックでは囲まずにそのまま出力して

---

# 差分:
    {diff}

---

# リポジトリのREADME:
    {readme}

---

# テンプレート:
```markdown
# 🚀 リリース {latest_tag}

## 🌟 主な変更点

ここに、このリリースの主要な変更点や新機能を3〜5行で簡潔に要約してください。

## ✨ 新機能

- 【重要度: 高】新機能1の簡潔な説明
- 【重要度: 中】新機能2の簡潔な説明
- 【重要度: 低】新機能3の簡潔な説明

## 🐛 バグ修正

- 修正されたバグ1の簡潔な説明
- 修正されたバグ2の簡潔な説明

## 🚀 パフォーマンス改善

- パフォーマンス改善1の簡潔な説明とその影響
- パフォーマンス改善2の簡潔な説明とその影響

## 💥 破壊的変更

- **[要注意]** 破壊的変更1の詳細な説明と対応方法
- **[要注意]** 破壊的変更2の詳細な説明と対応方法

## 📚 ドキュメント更新

- 更新されたドキュメント1の簡潔な説明
- 更新されたドキュメント2の簡潔な説明

## 🛠 その他の変更

- その他の小さな変更や改善点をリストアップ

## 🆙 アップグレード手順

1. ステップ1の説明
2. ステップ2の説明
3. ステップ3の説明

## 📝 注意事項

- 注意事項1の説明
- 注意事項2の説明

```

上記のテンプレートに基づいて、READMEを参考に、差分の内容のリリースノートを生成してください。
各セクションの内容は、提供された情報に基づいて適切に調整してください。
重要でないセクションは省略しても構いません。
READMEはまだ更新されていないのでリポジトリの内容を知るために活用して

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
