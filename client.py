#! /usr/bin/env python
import socket,datetime,time,math
PACKAGES_NUMBER = 10
SEND_INTERVAL_TIME = 1
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(("",8081))
s.bind(("",12345))
port = 8081
host = "127.0.0.1"#"219.245.125.59"
package_num = 0
delay =[]
sum_delay = 0
while True:
	t = datetime.datetime.now()
#	t = time.time()
#	s = time.mktime(time.strptime(t, '%Y-%m-%d %H:%M:%S'))
	msg = str(t)
	s.sendto(msg,(host,port))
	data,addr=s.recvfrom(1024)
	t = datetime.datetime.now()
	ms_str_send = data[-7:-4]
	ms_str_recv = str(t)[-6:-3]
	ms_int_send = int(ms_str_send)
	ms_int_recv = int(ms_str_recv)
	print "number: "+str(package_num)
	print data,"from",addr
	print str(t)
	print ms_str_send + " " + ms_str_recv
	if(ms_int_recv<ms_int_send):
		ms_int_recv += 1000
	delay.append(ms_int_recv - ms_int_send)
	sum_delay += delay[package_num]
	print delay[package_num]
	print "\n"
	package_num+=1
	if package_num >= PACKAGES_NUMBER:
	 break
	time.sleep(SEND_INTERVAL_TIME)
#print sumttl
for i in delay:
	print i
avarage_delay = float(sum_delay)/PACKAGES_NUMBER
print "Dalay Time: "+str(avarage_delay)
sum_squares = 0.0
for i in delay:
	sum_squares += (i-avarage_delay)**2
print sum_squares
evolution = math.sqrt(sum_squares/PACKAGES_NUMBER)
print ": "+str(evolution)
