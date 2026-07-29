import socket

# 1. 创建socket对象
socket_server = socket.socket()
# 2. 绑定ip地址（在哪台机器）和端口（哪个程序）
# 192.168.1.100:8000 网络服务
socket_server.bind(("localhost", 8888))
# 3. 服务器开始监听
# 1代表允许多少个连接
socket_server.listen(1)
# 4. 接收客户端连接 获取连接对象
# accept()是一个阻塞函数
conn, address = socket_server.accept()
print(f"Connexion du client reçue, connexion de {address}.")

while True:
    # 接收客户发的信息
    data = conn.recv(1024).decode("UTF-8")
    if data == "exit":
        break

    print(data)
    reply = input("Veuillez saisir un message de réponse: ").encode("UTF-8")
    conn.send(reply)

conn.close()
socket_server.close()