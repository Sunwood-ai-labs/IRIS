import os
import shutil
from git import Repo
from loguru import logger
from art import *

class IrisCoon:
    def __init__(self, target_dir=None, force=False, exclude_files=None):
        self.target_dir = target_dir or os.getcwd()
        self.cache_dir = os.path.expanduser("~/.cache/iris")
        self.repo_url = "https://github.com/Sunwood-ai-labs/IRIS"
        self.force = force
        self.exclude_files = exclude_files or []
        logger.add("iris_coon.log", rotation="10 MB")
        tprint('Iris Coon')
        self._log_parameters()

    def _log_parameters(self):
        logger.info("======== パラメータ ========")
        logger.info(f"> ターゲットディレクトリ: {self.target_dir}")
        logger.info(f"> 強制上書き: {'有効' if self.force else '無効'}")
        logger.info(f"> 除外ファイル: {', '.join(self.exclude_files) if self.exclude_files else 'なし'}")
        logger.info("==========================")

    def clone_repo(self):
        logger.info("リポジトリのクローン/更新を開始します...")
        if not os.path.exists(self.cache_dir):
            logger.info(f"IRISリポジトリを{self.cache_dir}にクローンしています...")
            Repo.clone_from(self.repo_url, self.cache_dir)
        else:
            logger.info(f"{self.cache_dir}のIRISリポジトリを更新しています...")
            repo = Repo(self.cache_dir)
            origin = repo.remotes.origin
            origin.pull()
        logger.success("リポジトリのクローン/更新が完了しました")

    def copy_github_folder(self):
        logger.info(".githubフォルダのコピーを開始します...")
        src = os.path.join(self.cache_dir, ".github")
        dst = os.path.join(self.target_dir, ".github")
        
        if os.path.exists(src):
            logger.info(".githubフォルダをターゲットディレクトリにコピーしています...")
            self._copy_tree(src, dst)
            logger.success(".githubフォルダのコピーが完了しました")
        else:
            logger.error("IRISリポジトリに.githubフォルダが見つかりません")

    def run(self):
        logger.info("IRIS Coon - IRISリポジトリクローンツールを開始します")
        self.clone_repo()
        self.copy_github_folder()
        self._log_copied_files()
        logger.success("IRIS Coonの処理が完了しました")

    def _copy_tree(self, src, dst):
        if self.force:
            shutil.rmtree(dst, ignore_errors=True)
        
        def _ignore_files(dir, files):
            return [f for f in files if f in self.exclude_files]

        shutil.copytree(src, dst, dirs_exist_ok=self.force, ignore=_ignore_files)

    def _log_copied_files(self):
        logger.info("コピーされたファイルとフォルダ:")
        github_dir = os.path.join(self.target_dir, ".github")
        for root, dirs, files in os.walk(github_dir):
            level = root.replace(github_dir, '').count(os.sep)
            indent = '│   ' * (level - 1) + '├── ' if level > 0 else ''
            logger.info(f"{indent}{os.path.basename(root)}/")
            sub_indent = '│   ' * level + '├── '
            for i, file in enumerate(files):
                if i == len(files) - 1:
                    sub_indent = '│   ' * level + '└── '
                if file not in self.exclude_files:
                    logger.info(f"{sub_indent}{file}")
                else:
                    logger.info(f"{sub_indent}{file} (除外)")
        
        if self.exclude_files:
            logger.info("除外されたファイル:")
            for file in self.exclude_files:
                logger.info(f"・ {file}")

if __name__ == "__main__":
    # 除外したいファイルのリストを指定
    exclude_list = ["config.yml", "test.yml"]
    iris_coon = IrisCoon(target_dir="/path/to/target", force=True, exclude_files=exclude_list)
    iris_coon.run()
