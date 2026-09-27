# 目标：给一个文件夹，把这个文件夹以及所有子文件夹里的文件全部找出来
import os

def get_files_recursion_from_dir(path):
    print("Le dossier actuel est: " + path)

    # 保存我们找到的所有文件
    file_list = []

    # 判断文件夹是否存在
    if os.path.exists(path):
        # 找到当前文件夹里的内容
        for f in os.listdir(path):
            # new_path = path + "/" + f
            # 拼接路径，兼容不同操作系统
            new_path = os.path.join(path, f)
            # 判断是否是文件夹
            if os.path.isdir(new_path):
                file_list += get_files_recursion_from_dir(new_path)
            else:
                file_list.append(new_path)

    else:
        print(f"Le répertoire spécifié {path} n'existe pas.")
        return []

    return file_list

if __name__ == "__main__":
    files = get_files_recursion_from_dir("/Users/citron/Documents/GitHub/PythonMaster3/Chapter3/Course")
    print(files)