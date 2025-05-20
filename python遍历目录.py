import os

def traverse_folder(root_dir):
    for root, dirs, files in os.walk(root_dir):
        # root: 当前目录路径
        # dirs: 当前目录下的子目录列表
        # files: 当前目录下的文件列表
        for file in files:
            file_path = os.path.join(root, file)
            print(f"文件: {file_path}")
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            print(f"目录: {dir_path}")

# 示例
traverse_folder("/Users/pengchaoma")