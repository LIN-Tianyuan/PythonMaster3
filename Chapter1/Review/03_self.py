# 定义类
class Car:
    # 定义方法
    def run(self):
        # 打印self的值
        print(f"self的值:{self}")
        print("能跑起来了...")

# 创建对象：对象名 = 类名()
car = Car()
# 输出对象结果
print(f"输出car对象名：{car}")
car.run()

# 创建对象2
my_car = Car()
print(f"输出my_car对象名：{my_car}")
my_car.run()

# car调用run()时，self和car的地址一样
# my_car调用run()时，self和my_car的地址一样
# 结论：谁调用方法，self就代表谁