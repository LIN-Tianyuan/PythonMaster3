from pymysql import Connection

# 创建一个连接
conn = Connection(
    host="localhost",        # IP地址,
    port=3306,               # 端口
    user='root',             # 登陆用户
    password='alex4869',     # 密码
    database='class2',       # 数据库
    autocommit=True          # 自动提交
)

# 获取登陆信息
print(conn.get_server_info())

# 获取一个游标对象cursor
cursor = conn.cursor()
# 创建student2表
# cursor.execute("create table student2(id int,name varchar(20),age int,gender varchar(10));")
# 插入数据
# cursor.execute("insert into student2 values (10001, 'Leo', 18, 'male'), (10002, 'Kevin', 21, 'male');")
# 只有增删改需要commit()
# conn.commit()

# 查询数据
# execute() 执行sql语句
cursor.execute("select * from student2;")
# fetchall() 获取一个查询的所有结果 返回值类型是tuple
results: tuple = cursor.fetchall()
for r in results:
    print(r)

# 关闭连接
conn.close()