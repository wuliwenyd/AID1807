#broadcast_send.py
from socket import *
from time import sleep

dest = ('176.136.17.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

