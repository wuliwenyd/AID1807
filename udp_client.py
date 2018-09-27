#udp_client.pysdfdjskfjdksfjkdskdsfjdksj
from socket import *
import sys


if len(sys.argv) < 3:
    print("argv is error!")

    raise

HOST = sys.argv[1]
PORT = int(sys.argv[2])
ADDR = (HOST,PORT)

sockfd = socket(AF_INET,SOCK_DGRAM)

while True:
    data=input("发送>>")
    if not data:
        break
    sockfd.sendto(data.encode(),ADDR)
    data,addr=sockfd.recvfrom(1024)
    print("从服务器收到:",data.decode())

sockfd.close()
