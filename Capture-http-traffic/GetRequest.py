#coding:utf-8

from socket import *

s = socket(AF_INET,SOCK_STREAM)
s.bind(('127.0.0.1',8080))
s.listen(1)
sock,addr = s.accept()
data = sock.recv(1024)
print data
sock.close()
s.close()
