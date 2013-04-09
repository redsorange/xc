#! /usr/bin/env python
import socket,datetime
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(("",8081))
#port=12344
#host=""
while True: 

	data,addr = s.recvfrom(1024)

#t1 = datetime.datetime.now()
	print "Received:",data,"from",addr
	
#	t2 = datetime.datetime.now()
#msg = data+" received "+str(t1) + " sended "+str(t2)
	msg = data+"\n"#+str(t2)+"\n"
	s.sendto(msg,addr)

