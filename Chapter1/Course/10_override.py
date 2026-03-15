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
        print("Child 5g calls.")


my_phone = MyPhone()
print(my_phone.producer)
print(my_phone.face_id)
my_phone.call_by_5g()

# Override：重写父类的属性和行为