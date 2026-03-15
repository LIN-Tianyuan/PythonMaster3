class Phone:
    serial_number = None
    producer = "Huawei"

    def call_by_5g(self):
        print("5g calls.")

class NFCReader:
    nfc_type = "Fifth Generation"
    producer = "HM"

    def read_card(self):
        print("Read NFC cards.")

    def write_card(self):
        print("Write NFC cards.")

class RemoteControl:
    rc_type = "IR remote control"

    def control(self):
        print("Infrared remote control opening.")

class MyPhone(NFCReader, Phone, RemoteControl):
    pass

xiaomi_phone = MyPhone()
xiaomi_phone.call_by_5g()
xiaomi_phone.control()
# 如果父类有相同属性或行为，会默认从左到右的顺序获取
print(xiaomi_phone.producer)