# Python Master

## Chapter 1 面向对象

### 1. 类和对象

- 类里有两部分
  - 属性（成员变量）
  - 行为（成员方法）
- 注：函数在类里叫方法（特征：有self）
- 类是程序中的“蓝图”，必须基于它们生成实体（对象）才能正常运行。
- 这种方法被称为：面向对象编程！(Object-oriented programming)

```python
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
```

### 2. self

- self：代表对象本身
- self会出现在形式参数列表中，但是不占位（会被忽略）

```python
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
```

### 3. 构造方法

- \_\_init\_\_
- 当创建对象的时候会自动执行
- 创建对象的时候传参数，会自动传递到\_\_init\_\_构造方法

```python
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
```

### 4. 魔法方法

```bash
__init__  构造方法，用于创建类对象的时候设置初始化行为
__str__   用于实现类对象转字符串的行为
__lt__    用于2个类对象进行小于或大于比较
__le__    用于2个类对象进行小于等于或大于等于比较
__eq__    用于2个类对象进行相等比较
```

### 5. 三大特性

#### 5.1 封装

- 在类中对现实世界中的元素（如属性与方法）进行描述，这一概念被称为封装

- 私有成员变量、私有成员方法
  - 以\_\_开头的变量或方法
  - 对象不能访问私有成员（变量与方法）
  - 但是类里的其他成员可以访问同类的私有成员

```python
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
```

#### 5.2 继承

- 继承是指一个类继承了另一个类的成员变量和成员方法
- 单继承

```python
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
```

- 多继承

```python
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
```

- 重写（override）
  - 重写父类的成员属性或成员方法

```python
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
```

#### 5.3 多态

- 多态性意味着，使用不同的对象实现不同的行为，可以得到不同的状态
- 例如，定义一个函数（方法），通过类型注解声明它需要父类的对象，但在实际调用时传入子类的对象来执行操作，从而得到不同的运行状态

- 抽象方法：一个方法如果空实现（只有pass），它就是抽象方法。
- 抽象类：只有抽象方法的类叫抽象类。

```python
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
```

## Chapter 2 SQL

## Chapter 3 Python 高级

## Chapter 4 Git

### 1. 版本控制器

- 集中式（SVN）：版本库集中存放在中央服务器上。必须联网才能工作。
- 分布式（Git）：每个人的电脑上都是一个完整的版本库，包含全部历史。工作时不需要联网。

### 2. Git的历史

- Git是一个开源的分布式版本控制系统，由Linux之父Linus Torvalds为管理Linux内核开发而创建。

### 3. Git工作流程

- 工作区：Workspace，修改代码的地方
- 暂存区：Index/Stage，在`.git`目录中，准备提交的修改清单
- 本地仓库：Repository，在`.git`目录中，所有已提交版本的历史
- 远程仓库：Remote，在服务器上（Github, Gitee），与团队共享的交换点

七个命令：

- `clone`：从远程仓库中克隆代码到本地仓库
- `checkout`：从本地仓库检出一个分支到工作区进行修订
- `add`：提交前先把修改放进暂存区
- `commit`：把暂存区提交到本地仓库。本地仓库保存每一个历史版本
- `fetch`：把远程仓库的更新抓取到本地仓库，不做任何合并，平时用得较少
- `pull`：从远程仓库拉到本地并自动合并到当前分支。`pull` = `fetch` + `merge`
- `push`：修改完成、需要和团队共享时，把代码推送到远程仓库

### 4. 基础命令

- `git init`：获取本地仓库
- `git add 文件名`：把文件的修改加入暂存区
- `git add .`：把所有修改加入暂存区
- `git commit -m "注释内容"`： 把暂存区提交到本地仓库的当前分支
- `git log`：查看提交记录
- `git reset --hard commitID`：版本回退（切换到指定版本）
- `git reflog`：查看已被删除的提交记录
- `git status`：查看修改的状态（暂存区、工作区）

### 5. 基础操作

```bash
# 初始化 git 仓库
git init

# 创建文件 file01.txt
# touch file01.txt
# 然后
git add .
git commit -m 'commit 001'
# 看到提交的记录
git log

# 把 file01.txt 内容改为 count=1，然后：
git add .
git commit -m 'update file01'
# 看到两条提交的记录
git log

# 将最后一次修改还原：
# 用 git log 找到你要还原的地方提交的commitID，然后
git reset --hard commitID

# 这时可以看到文件已恢复为空
cat file01.txt
```

### 6. 分支

#### 6.1 分支命令

- `git branch`: 查看本地分支
- `git branch 分支名`：创建本地分支
- `git checkout 分支名`：切换分支
- `git checkout -b 分支名`：创建并切换到新分支
- `git merge 分支名称`：把某分支合并到当前分支
- `git branch -d b1`：删除分支（做各种检查）

#### 6.2 分支操作

```bash
# 创建分支 dev01 并切换过去
git branch dev01
git checkout dev01
# git checkout -b dev01

# 创建文件 file02.txt
# touch file02.txt
# 然后
git add .
git commit -m 'add file02 on dev'
# 看到提交的记录
git log

# 切回main，合并dev01
git checkout main
git merge dev01
git log

# 删除 dev01 分支
git branch -d dev01
git log
```

### 7. 远程仓库

#### 7.1 常用的托管服务

`GitHub`：面向开源及私有项目的托管平台，只支持`Git`作为版本库格式，故名`Github`

`GitLab`：开源的仓库管理系统，一般用于在企业、学校等内部网络搭建`Git`私服

#### 7.2 注册Github并创建远程仓库

- `https://github.com` 注册账号，新建仓库
- 输入仓库名称（`git_test`），填写仓库介绍
- 选择**私有**或**公开**
- 点击**创建**

#### 7.3 配置SSH公钥

配置SSH公钥后，Github就能识别你，不用每次输入密码。

```bash
# 1.生成 SSH 公钥（一路回车）
ssh-keygen -t rsa
# 如果公钥已经存在，会自动覆盖

# 2.查看并复制公钥
cat ~/.ssh/id_rsa.pub

# 3. 在Github上，头像->设置->SSH and GPG keys，粘贴公钥，起个标题，点击确定
# 4. 验证是否配置成功
ssh -T git@github.com

# Hi LIN-Tianyuan! You've successfully authenticated, but GitHub does not provide shell access.
```

#### 7.4 远程仓库操作

```bash
# 1.将本地仓库推送到远程仓库
# [test]
cd test
# 给本地仓库登记一个远程仓库地址，并起名叫origin
git remote add origin git@github.com:LIN-Tianyuan/git_test.git
# 把本地的main分支推送到origin远程仓库
# --set-upstream(简写-u)会把本地main和远程的main关联起来
# 之后再推送或拉取，只需要输入git push/git pull，不用每次都写origin main
git push --set-upstream origin main

# 2.将远程仓库克隆到本地 git_test
git clone git@github.com:LIN-Tianyuan/git_test.git

# 3.将本地修改推送到远程仓库
# [git_test]
git add .
git commit -m "add file03"
git push origin main

# 4.将远程仓库的修改更新到本地
git pull
```



