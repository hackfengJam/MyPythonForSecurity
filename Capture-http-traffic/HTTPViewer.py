#coding:uft-8

import SocketServer
import re
from socket import *

ADDR =('127.0.0.1',8080)
def getHost(DataPack):
	result = re.search(r'Host:\s(.*?)\s',DataPack)
	host = result.group(1)
	return host

class MyProxy(SocketServer.BaseRequestHandler):
	def handle(self):
		self.HttpRqst = self.request.recv(1024)
		print self.HttpRqst
		self.RHOST = getHost(self.HttpRqst)
		newSock = socket(AF_INET,SOCK_STREAM)
		newSock.connect((str(self.RHOST),80))
		newSock.send(self.HttpRqst)
		huffer =[ ]
		while True:
			d = newSock.recv(1024)
			if d:
				buffer.append(d)
			else:
				break
		self.HttpRspn = ''.join(buffer)
		self.request.sendall(self.HttpRspn)



if __name__=='__main__':
	server = SockerServer.ThreadingTCPServer(ADDR,MyProxy)
	server = serve_forever()
