from iris_coon import IrisCoon

if __name__ == "__main__":
    # 除外したいファイルのリストを指定
    exclude_list = ["publish-to-pypi.yml"]
    iris_coon = IrisCoon(target_dir=r"C:\Prj\iris_demo2", force=True, exclude_files=exclude_list)
    iris_coon.run()
