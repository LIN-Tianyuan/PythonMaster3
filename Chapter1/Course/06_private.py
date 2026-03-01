class Phone:
    # 公共变量（公开成员属性）
    serial_number = None        # 序列号
    producer = None             # 生产商

    # 私有变量（私有成员属性）
    # 以__开头
    __current_voltage = 0    # 目前电压

    # 公共方法（公开成员方法）
    # 私有成员（变量和方法）不能被对象调用，但是可以被类里其他成员（变量和方法）调用
    def call_by_5g(self):
        if self.__current_voltage >= 1:
            self.__keep_single_core()
            print("Les appels 5g sont désormais possible.")
        else:
            print("Défaut d'appel, batterie faible.")

    # 私有方法（私有成员方法）
    def __keep_single_core(self):
        print("Faire fonctionner l'unité centrale en mode mono-coeur pour économiser de l'énergie.")

phone = Phone()
phone.call_by_5g()
# 私有成员变量不能被对象使用
# phone.__current_voltage = 50
# print(phone.__current_voltage)
# 私有成员方法不能被对象调用
# phone.__keep_single_core()

# 面向对象三大属性之一：封装



