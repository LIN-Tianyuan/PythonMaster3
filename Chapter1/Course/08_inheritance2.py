class Phone:
    serial_number = None
    producer = None

    def call_by_4g(self):
        print("4g calls.")

class Phone2026(Phone):
    face_id = True

    def call_by_5g(self):
        print("2026 latest 5g calls.")

phone2026 = Phone2026()
phone2026.producer = "Apple"
phone2026.call_by_4g()
phone2026.call_by_5g()

# 面向对象三大属性之二：继承
# 单继承：
# class 类名（父类名）：
#       新类的属性和方法
# 继承分为单继承（主要）和多继承
# 继承会把父类的公开的成员变量和方法都拿过来，直接可以用
# 多继承：
# class 类名（父类名1, 父类名2, ..., 父类名n）：
#       新类的属性和方法