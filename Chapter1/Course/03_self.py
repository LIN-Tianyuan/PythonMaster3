# 定义类
class Student:
    name = None
    age = None

    def say_hi(self):
        print(f"Bonjour à tous, je m'appelle {self.name} et j'ai {self.age} ans.")

    def say_hi2(self, msg="666"):
        print(f"Bonjour à tous, {msg}")

# 创建对象
student = Student()
student.name = "Alex"
student.age = 18
student.say_hi()
student.say_hi2("enchanté de vous rencontrer.")

