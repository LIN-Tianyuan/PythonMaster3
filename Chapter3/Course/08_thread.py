# 多线程：一个程序里同时运行多个线程（Thread），让多个任务看起来能够同时执行。

# Process 进程（程序）：一家餐厅
# Thread 线程：餐厅里的员工

# 餐厅（一个进程）：服务员A(线程1），服务员B（线程2），洗碗工，厨师..
# 线程的特点：共享同一块内存，所以通信方便
# 为什么需要多线程？
# 例如下载文件，如果不用多线程：下载A -> 下载B -> 下载C (3 + 3 + 3) = 9秒
# 如果多线程：3秒（同时开始）效率大大提高

import threading
import time

def sing():
    while True:
        print("我在唱歌。")
        time.sleep(1)

def dance():
    while True:
        print("我在跳舞。")
        time.sleep(1)

# 两个线程一起运行
sing_thread = threading.Thread(target=sing)
dance_thread = threading.Thread(target=dance)

sing_thread.start()
dance_thread.start()

# 结论：可以看到两个任务交替执行
