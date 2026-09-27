# 递归：一个函数调用它自己
# 终止条件(Cas de base) 递归调用(Appel récursif)

import os

def test_os():
    # 查看文件夹里面有什么，listdir：列出目录内容
    print(os.listdir("/Users/citron/Documents/GitHub/PythonMaster3/Chapter3/Course"))
    # 判断是否是文件夹
    print(os.path.isdir("/Users/citron/Documents/GitHub/PythonMaster3/Chapter3/Course"))
    # 判断路径是否存在
    print(os.path.exists("/Users/citron/Documents/GitHub/PythonMaster3/Chapter3/Course"))

test_os()