# 闭包的核心: 不仅能执行代码 还能”记住“创建时的环境和配置
def outer(logo):
    def inner(msg):
        print(f"<{logo}>{msg}<{logo}>")

    return inner

fn1 = outer("SCEF Formation")
fn1("Hello")
fn1("World")

fn2 = outer("Phone")
fn2("Huawei")
fn2("Apple")