# 闭包
account_amount = 0  # 账户余额

def atm(num, deposit=True):
    global account_amount
    if deposit:
        account_amount += num
        print(f"存入：+ {num}, 余额：{account_amount}")
    else:
        account_amount -= num
        print(f"取出：+ {num}, 余额：{account_amount}")

"""
atm(300)
atm(300)
atm(100, False)
"""

def account_create(initial_amount = 0):
    def atm(num, deposit=True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存入：+ {num}, 余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"取出：- {num}, 余额：{initial_amount}")
    return atm

fn = account_create(100)
fn(300)
fn(300)
fn(100, False)
