import os
import sys
import subprocess
import yaml

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from loguru import logger
from config import get_settings
from services.llm_service import LLMService
from services.github_service import GitHubService

def run_command(cmd):
    logger.info(f"実行コマンド: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    if result.returncode != 0:
        logger.error(f"コマンド実行エラー: {result.stderr}")
    logger.info(f"コマンド出力: {result.stdout}")
    return result.stdout

def run_sourcesage():
    cmd = f"sourcesage --ignore-file=.iris.SourceSageignore"
    run_command(cmd)

def update_yaml_file(latest_tag):
    yaml_path = 'docs/.sourcesage_releasenotes_iris.yml'
    logger.info(f"YAMLファイルを更新: {yaml_path}")
    with open(yaml_path, 'r') as file:
        data = yaml.safe_load(file)
    
    data['repo-version'] = latest_tag
    data['docuMind-release-report'] = f".SourceSageAssets/RELEASE_REPORT/Report_{latest_tag}.md"
    data['docuMind-output'] = f".SourceSageAssets/DOCUMIND/RELEASE_NOTES_{latest_tag}.md"
    data['docuMind-prompt-output'] = f".SourceSageAssets/DOCUMIND/_PROMPT_{latest_tag}.md"
    
    with open(yaml_path, 'w') as file:
        yaml.dump(data, file)
    logger.info(f"YAMLファイルを更新しました: {yaml_path}")

def generate_prompt(latest_tag):
    
    changelog_path = ".SourceSageAssets/Changelog/CHANGELOG_main.md"
    
    if not os.path.exists(changelog_path):
        logger.warning(f"ファイルが見つかりません: {changelog_path}")
        logger.info(".SourceSageAssetsフォルダのファイルツリーを表示します:")
        
        try:
            tree_command = "tree .SourceSageAssets" if os.name != 'nt' else "tree /f /a .SourceSageAssets"
            result = subprocess.run(tree_command, shell=True, check=True, capture_output=True, text=True)
            logger.info(result.stdout)
        except subprocess.CalledProcessError as e:
            logger.error(f"ファイルツリーの表示中にエラーが発生しました: {e}")
            logger.info("代替方法でファイル一覧を表示します:")
            for root, dirs, files in os.walk(".SourceSageAssets"):
                level = root.replace(".SourceSageAssets", "").count(os.sep)
                indent = " " * 4 * level
                logger.info(f"{indent}{os.path.basename(root)}/")
                sub_indent = " " * 4 * (level + 1)
                for file in files:
                    logger.info(f"{sub_indent}{file}")
    else:
        logger.info(f"ファイルが見つかりました: {changelog_path}")

    cmd = f"sourcesage --ss-mode=DocuMind --yaml-file=docs/.sourcesage_releasenotes_iris.yml"
    run_command(cmd)
    
    prompt_path = f".SourceSageAssets/DOCUMIND/_PROMPT_{latest_tag}.md"
    logger.info(f"生成されたプロンプトを読み込み: {prompt_path}")
    with open(prompt_path, 'r') as file:
        prompt = file.read()
    logger.info(f"プロンプトの長さ: {len(prompt)} 文字")
    return prompt

def main():
    logger.info("GitHub リリースノート生成プロセスを開始します。")
    
    settings = get_settings()
    llm_service = LLMService()
    github_service = GitHubService()

    latest_tag = os.getenv('LATEST_TAG', '')

    if not latest_tag:
        logger.error("環境変数 'LATEST_TAG' が設定されていません。")
        sys.exit(1)

    logger.info(f"最新のタグ: {latest_tag}")

    run_sourcesage()
    update_yaml_file(latest_tag)
    prompt = generate_prompt(latest_tag)

    logger.info("LLMを使用してリリースノートを生成します。")
    logger.debug(f"リリースノート生成プロンプト：{prompt}")
    release_notes = llm_service.get_response(prompt)
    logger.info(f"リリースノートの生成が完了しました。長さ: {len(release_notes)} 文字")

    try:
        github_service.create_release(latest_tag, release_notes)
        logger.info(f"GitHubリリース {latest_tag} を作成しました。")
    except Exception as e:
        logger.error(f"GitHubリリースの作成中にエラーが発生しました: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
