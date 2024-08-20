import os

def prepare_dir():
    dir_name = 'save_dir'
    if os.path.exists(dir_name):
        print(f"{dir_name} はすでに存在します。")
    else:
        os.makedirs(dir_name)
        print(f"{dir_name} を作成しました。")

prepare_dir()
