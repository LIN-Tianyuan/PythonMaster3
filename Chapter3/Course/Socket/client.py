import socket

# 1. 创建socket对象
socket_client = socket.socket()
# 2. 连接服务器
socket_client.connect(("localhost", 8888))
# 3. 发送信息
while True:
    send_msg = input("Veuillez saisir le message à envoyer: ")
    if send_msg == 'exit':
        break

    socket_client.send(send_msg.encode("UTF-8"))
    recv_data = socket_client.recv(1024)
    recv_data = recv_data.decode("UTF-8")
    print(f"Le serveur répond en envoyant le message suivent: {recv_data}")

socket_client.close()