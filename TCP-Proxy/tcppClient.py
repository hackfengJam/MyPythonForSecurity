#coding:utf-8

from socket import *
import sys

HOST = '127.0.0.1'
PORT = int(sys.argv[1])

c = socket(AF_INET,SOCK_STREAM)
c.connect((HOST,PORT))
print 'Connected success' 
c.send('Yes or No')
text = c.recv(1024)
print text
c.close()
