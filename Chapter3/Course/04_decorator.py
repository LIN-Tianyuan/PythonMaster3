"""
原始函数
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1, 5))
"""

def sleep():
    import random
    import time
    print("我要睡觉了！")
    print("Sleeping...")
    time.sleep(random.randint(1, 5))
    print("我起床了！")

if __name__ == "__main__":
    sleep()