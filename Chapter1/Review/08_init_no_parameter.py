# 定义类
class Car:
    # 初始化：无参数，类内部直接赋值
    # 创建对象时自动调用，初始化属性值
    def __init__(self):
        self.color = "Black"
        self.number = 3

    # 类内部获取属性：self.属性
    def show(self):
        print(f"车的颜色为：{self.color}")
        print(f"车的轮胎个数为:{self.number}")

car = Car()
# 类外部访问属性：对象名.属性
print(f"类外部访问属性：{car.color}")
# 调用方法：对象名.方法名()
car.show()