def outer(func):
    def inner():
        print("我要睡觉了！")
        func()
        print("我起床了！")
    return inner

# 装饰器 decorator
# 实际上执行 sleep = outer(sleep) 即 func = sleep
@outer
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1, 5))

sleep()

# 装饰器语法糖版本
# python在加载代码时，会自动转换成：
"""
def sleep():
    import random
    import time
    print("Sleeping...")
    time.sleep(random.randint(1, 5))
    
sleep = outer(sleep)
"""

# 为什么需要装饰器？因为不用改原函数。
# 装饰器（Decorator）就是在不修改原函数代码的情况下，给函数增加新功能。

class Tool:
    pass

t1 = Tool()
t2 = Tool()
print(t1)
print(t2)
print(t1 == t2)