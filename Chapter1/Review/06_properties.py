# 定义类
class Car:
    # 定义方法
    def run(self):
        print("能跑起来了...")

# 创建对象
car = Car()
# 类外部
# 添加属性：对象名.属性 = 属性值
car.color = "红色"
car.number = 4

# 获取属性：对象名.属性
print(f"车的颜色:{car.color}")
print(f"轮胎数：{car.number}")