class Animal:
    # 在父类只定义一个方法 不实现
    def speak(self):
        pass

class Dog(Animal):
    # 具体实现交给子类去重写
    def speak(self):
        print("Woof woof woof")

class Cat(Animal):
    def speak(self):
        print("Miaou miaou miaou")

def make_noise(animal: Animal):
    animal.speak()

dog = Dog()
make_noise(dog)

cat = Cat()
make_noise(cat)

# 多态必须基于继承。
# 父类只用来定义方法 在方法里做空实现
# 再由子类去做实现
# 此时这个类就叫做抽象类 里面的方法叫做抽象方法