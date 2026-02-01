# 创建一个学生类
# class 类名：
#    属性
#    行为
class Student:
    # 属性（成员变量）：名字
    name = None
    age = None

    # 行为（成员方法）

# 创建对象
# 格式：对象名 = 类名()
stu_1 = Student()
stu_2 = Student()
# 给对象设置具体属性 名字为Leo
stu_1.name = "Leo"
stu_1.age = 18
stu_2.name = "Laurent"
stu_2.age = 19
print(stu_1.name)
print(stu_1.age)
print(stu_2.name)
print(stu_2.age)