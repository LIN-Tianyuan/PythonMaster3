import threading
import time

def sing():
    while True:
        print("我在唱歌。")
        time.sleep(1)

def dance(message):
    while True:
        print(message)
        time.sleep(1)

# 两个线程一起运行
# 创建线程对象
sing_thread = threading.Thread(target=sing)
# keyword
dance_thread = threading.Thread(target=dance, kwargs={"message": "我在跳舞。"})

sing_thread.start()
dance_thread.start()

# 结论：可以看到两个任务交替执行
