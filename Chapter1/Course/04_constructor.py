# 创建类
class Student:
    # 成员变量
    name = None
    age = None
    tel = None

    # 构造方法（魔法方法）
    # 在创建对象的时候会自动调用此方法
    def __init__(self, name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("La classe Etudiant crée un objet.")

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

stu = Student("Alex", 18, "110")
print(stu.name)
"""
# 创建对象
stu_1 = Student()
stu_1.name = "Alex"
stu_1.age = 18
stu_1.tel = "110"

stu_2 = Student()
stu_2.name = "Luna"
stu_2.age = 19
stu_2.tel = "120"
"""