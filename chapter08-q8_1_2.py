import os

def delete_dir():
    dir_name = 'save_dir'
    if os.path.exists(dir_name):
        print(f"{dir_name} が存在します。")
        os.rmdir(dir_name)
        print(f"{dir_name} を削除しました。")
    else:
        print(f"{dir_name} は存在しません。")

delete_dir()

