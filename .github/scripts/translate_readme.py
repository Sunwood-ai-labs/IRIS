import os
import sys

# Add the parent directory of 'scripts' to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger
from config import get_settings
from services.llm_service import LLMService

def main():
    logger.info("README翻訳プロセスを開始します。")

    settings = get_settings()
    llm_service = LLMService()

    # READMEの内容を取得
    with open("README.md", "r", encoding="utf-8") as f:
        readme_content = f.read()

    # LLMに日本語のREADMEの英訳を依頼
    prompt = f"""
Please translate the following Japanese README into English:

```
{readme_content}
```
    """

    logger.info("LLMにREADMEの英訳を依頼しています...")
    translated_readme = llm_service.get_response(prompt)

    # 翻訳されたREADMEの内容をファイルに書き込む
    with open("README.en.md", "w", encoding="utf-8") as f:
        f.write(translated_readme)

    logger.info("READMEの英訳が完了しました。")

if __name__ == "__main__":
    main()
