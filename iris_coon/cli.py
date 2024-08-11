import argparse
from .core import IrisCoon

def main():
    parser = argparse.ArgumentParser(
        description="IRISリポジトリをクローンし、.githubフォルダと関連ファイルをコピーします。"
    )
    parser.add_argument(
        "--target", "-t",
        default=None,
        help="ファイルをコピーするターゲットディレクトリ。指定しない場合は現在の作業ディレクトリが使用されます。"
    )
    parser.add_argument(
        "--force", "-f",
        action="store_true",
        help="既存のファイルを強制的に上書きします。"
    )
    parser.add_argument(
        "--exclude", "-e",
        nargs="+",
        default=["publish-to-pypi.yml"],
        help="コピーから除外するファイルのリスト。スペース区切りで複数指定可能。"
    )

    args = parser.parse_args()

    coon = IrisCoon(target_dir=args.target, force=args.force, exclude_files=args.exclude)
    coon.run()

if __name__ == "__main__":
    main()
