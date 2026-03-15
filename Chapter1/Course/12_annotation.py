import random
import json

from typing import Union

# 基本数据类型注解
var_1: int = 10
var_2: float = 3.14
var_3: bool = True
# var_4: str = "Python"

# 对象数据类型注解
class Student:
    pass

stu: Student = Student()

# 容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"age": 18}
my_str: str = "python"

my_list2: list[int] = [1, 2, 3]
my_tuple2: tuple[str, int, bool] = ("age", 18, True)
my_set2: set[int] = {1, 2, 3}
# dict[str, int] str代表键的类型，int代表值的类型
my_dict2: dict[str, int] = {"age": 18, "num": 3}

var_4 = random.randint(1, 10)   # type: int
data = '{"age": 18}'
var_5 = json.loads(data)             # type: dict[str, int]
var_6 = Student()                    # type: Student

def add(x: int, y: int) -> int:
    return x + y

result = add(1, 2)
print(result)

def func(data: list[int]) -> list[int]:
    data.append(4)
    return data

l = [1, 2, 3]
d = func(l)
print(d)

my_list3 = [1, 2, "alex", "luna"]
my_dict3 = {"name": "alex", "age": 18}

my_list4: list[Union[str, int]] = [1, 2, "alex", "luna"]
my_dict4: dict[str, Union[str, int]] = {"name": "alex", "age": 18}

def func2(data: Union[int, str]) -> Union[int, str]:
    return data

r = func2(1)
print(r)