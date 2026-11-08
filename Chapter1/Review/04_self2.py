class Car:
    def run(self):
        print("能跑起来了...")

    # 若在类的内部调用方法：self.方法名()
    def work(self):
        # 跑起来
        self.run()

# 创建对象
car = Car()
# 工作
car.work()

# 在类外部，我们用对象名调用：car.run()
# 在类内部，还不知道对象叫什么名字，所以用self：self.run()
# 类外部：对象名.方法名()
# 类内部：self.方法名()