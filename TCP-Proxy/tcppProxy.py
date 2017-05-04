#coding:utf-8
from socket import *
from sys import *

def Usage():
	print "[Usage]toppProxy.py [LocalPort][RemoteServer][RemotePort]"

RemoteSocket = socket(AF_INET,SOCK_STREAM)	
MainSocket = socket(AF_INET,SOCK_STREAM)

def SetSocket(PORT):
	MainSocket.bind(('',PORT))
	MainSocket.listen(1)

def MainHandle():
	print ''
	
def ForwardData(data,RemoteServer,RemotePort):
	RemoteSocket.connect((RemoteServer,RemotePort))
	print 'Connected success to',RemoteServer,":",RemotePort
	RemoteSocket.send(data)
	result = RemoteSocket.recv(1024)
	RemoteSocket.close()
	return result

if __name__=='__main__':
	#try:
	print argv
	LPort = int(argv[1])
	DServer = argv[2]
	DPort = int(argv[3])
	SetSocket(LPort)
	while True:
		MainSock,addr = MainSocket.accept()
		print 'Connected by',addr
		data = MainSock.recv(1024)
		result = ForwardData(data,DServer,DPort)
		MainSock.send(result)
		MainSock.close()
	#except:
	Usage()
	
	
