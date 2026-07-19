# 闭包
account_amount = 0  # 账户余额

def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"存入：+ {num}, 余额：{account_amount}")
    else:
        account_amount -= num
        print(f"取出：- {num}, 余额：{account_amount}")

"""
atm(300)
atm(300)
atm(100, False)
"""

# 闭包：atm虽然已经被返回到外面，但仍然保存着 initial_amount 这个变量
def account_create(initial_amount = 0):
    # num: 金额， deposit=True 默认是存钱
    def atm(num, deposit=True):
        # 修改外层函数 account_create 中的 initial_amount
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存入：+ {num}, 余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取出：- {num}, 余额：{initial_amount}")
    # 返回的是函数本身
    return atm

# 返回的是atm函数
fn = account_create(100)
fn(300)
fn(300)
fn(100, False)
