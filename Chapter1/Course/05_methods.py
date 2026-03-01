class Student:
    name = None
    age = None

    # 魔法方法（被动触发）
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 修改对象创建后的打印
    def __str__(self):
        return f"name = {self.name}, age = {self.age}"

    # 以哪个属性作为两个对象的比较（小于lt、大于gt）可以只定义其中一个魔法方法即可
    def __lt__(self, other):
        return self.age < other.age

    # 以哪个属性作为两个对象的比较（小于等于le、大于等于ge）可以只定义其中一个魔法方法即可
    def __le__(self, other):
        return self.age <= other.age

    def __eq__(self, other):
        return self.age == other.age and self.name == other.name
    # 成员方法（主动触发）


student = Student("Alex", 18)
print(student)


student1 = Student("Alex", 18)
student2 = Student("Luna", 20)
student3 = Student("Hebe", 20)
student4 = Student("Alex", 18)
"""
print(student1 < student2)
print(student1 > student2)
print(student1 <= student2)
print(student2 <= student3)
print(student2 >= student3)
"""
print(student1 == student4)
print(student2 == student3)