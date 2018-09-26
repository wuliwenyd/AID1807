#tcp_server.py
from socket import *


sockfd = socket(AF_INET,SOCK_STREAM)

sockfd.bind(('0.0.0.0',8888))

sockfd.listen(5)

while True:
    connfd,addr=sockfd.accept()
    while True:
        data=connfd.recv(1024).decode()
        if not data:
            break
        print(data)
        n = connfd.send(b"receive from message")
        print("发送%d字节"%n)
    connfd.close()

sockfd.close()