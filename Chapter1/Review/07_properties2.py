# 定义类
class Car:
    # 定义方法
    def run(self):
        print("能跑起来了...")

    # 类内部获取属性：self.属性
    def show(self):
        print(f"车的颜色为：{self.color}")
        print(f"车的轮胎个数为:{self.number}")

car = Car()
car.color = "红色"
car.number = 4
car.show()

