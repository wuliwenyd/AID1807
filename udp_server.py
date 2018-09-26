#udp_server.py
from socket import *

sockfd = socket(AF_INET,SOCK_DGRAM)

server_addr = ('0.0.0.0',8888)
sockfd.bind(server_addr)

while True:
    data,addr = sockfd.recvfrom(1024)
    print("Receive from%s:%s"%(addr,data.decode()))
    sockfd.sendto('收到你的消息'.encode(),addr)

sockfd.close()