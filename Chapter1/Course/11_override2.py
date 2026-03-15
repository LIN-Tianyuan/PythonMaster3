class Phone:
    serial_number = None
    producer = "Huawei"

    def call_by_5g(self):
        print("Father 5g calls.")

class MyPhone(Phone):
    face_id = True
    producer = "Apple"

    # Override 重写
    def call_by_5g(self):
        # 场景：重写之后需要获取父类的属性或行为
        # 调用父类的属性：第一种
        print(f"La marque de la class pèré est: {Phone.producer}")
        # 调用父类的行为：第一种
        Phone.call_by_5g(self)

        # 调用父类的属性：第二种
        print(f"La marque de la class pèré est: {super().producer}")
        # 调用父类的行为：第二种
        super().call_by_5g()

my_phone = MyPhone()
my_phone.call_by_5g()
