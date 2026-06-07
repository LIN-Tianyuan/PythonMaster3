from data_define import Record
from file_define import TextFileReader, JsonFileReader
from pymysql import Connection

text_file_reader = TextFileReader("January2023SalesData.txt")
json_file_reader = JsonFileReader("February2023SalesData.txt")

jan_data: list[Record] = text_file_reader.read_data()
feb_data: list[Record] = json_file_reader.read_data()
all_data: list[Record] = jan_data + feb_data

"""
for data in all_data:
    print(data)
"""

# 创建数据库连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="alex4869",
    database='py_sql',
    # 自动提交
    autocommit=True
)

print(conn.get_server_info())

cursor = conn.cursor()

"""
for record in all_data:
    sql = f"insert into orders(order_date, order_id, money, province) values {record.date, record.order_id, record.money, record.province};"
    cursor.execute(sql)
"""

sql = "select * from orders;"

cursor.execute(sql)
results = cursor.fetchall()
for result in results:
    print(result)

conn.close()
