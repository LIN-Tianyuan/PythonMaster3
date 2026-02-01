# 创建类
class Student:
    # 成员变量
    name = None
    age = None

    # 成员方法
    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

# 创建对象
stu_1 = Student()
stu_1.name = "Alex"
stu_1.age = 18
stu_1.say_hi()

stu_2 = Student()
stu_2.name = "Luna"
stu_2.age = 19
stu_2.say_hi()