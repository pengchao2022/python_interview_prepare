#python 遍历指定目录下所有文件和文件夹

import os

def known_everythings(given_dir):

    for current_root, dirs, files in os.walk(given_dir):

        #current_root 表示当前目录路径
        #dirs 表示当前目录下的子目录列表
        #files 表示当前目录下的文件列表

        for file in files:
            file_path = os.path.join(current_root, file)
            print(f"这个是文件：{file_path}")

        for dir in dirs:
            dir_path = os.path.join(current_root, dir)
            print(f"这个是目录： {dir_path}")


#调用函数
known_everythings("/")
