#! /usr/bin/env python
import socket,datetime,time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(("",8081))
s.bind(("",12345))
port = 8081
host = "127.0.0.1"
#no = 1
while True:
	t = datetime.datetime.now()
	msg = str(t)
	s.sendto(msg,(host,port))
	data,addr=s.recvfrom(1024)
	t = datetime.datetime.now()
	print data,"from",addr
	print str(t)+"\n"
	time.sleep(1)
