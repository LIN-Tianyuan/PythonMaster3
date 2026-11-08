# 定义类
class Car:
    # 初始化：有参数，参数通过外部传递
    # 创建对象时自动调用，初始化属性值
    def __init__(self, color, number):
        self.color = color
        self.number = number

    # 类内部获取属性：self.属性
    def show(self):
        print(f"车的颜色为：{self.color}")
        print(f"车的轮胎个数为:{self.number}")

# 创建对象，并向__init__传递参数
car = Car("Red", 4)
# 获取属性值
print(car.number)
car.show()