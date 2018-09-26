#broadcast.py
from socket import *

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SQL_SOCKET,SO_BROADCAST,1)

s.bind(('0.0.0.0',8888))

while True:
    try:
        msg,addr = s.recvfrom(1024)
        print("从{}获取信息:{}".format(addr,msg.decode()))
    except (KeyboardInterrupt,SyntaxError):
        raise
    except Exception as e:
        print(e)

s.close()

