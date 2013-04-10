#! /usr/bin/env python
import socket,datetime,time,math
PACKAGES_NUMBER = 10
SEND_INTERVAL_TIME = 1
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#s.bind(("",8081))
s.bind(("",12345))
port = 8081
host = "127.0.0.1"#"219.245.125.59"
package_num = -1
delay =[]
sum_delay = 0
miss_package = 0
while True:
	package_num+=1
	if package_num >= PACKAGES_NUMBER:
	 break
	t = datetime.datetime.now()
	msg = str(t)
	s.sendto(msg,(host,port))
	try:
		s.settimeout(1)
		data,addr=s.recvfrom(1024)
		t = datetime.datetime.now()
	except socket.timeout:
		print "time out!"
		miss_package+=1
		continue
	ms_str_send = data[-7:-4]
	ms_str_recv = str(t)[-6:-3]
	ms_int_send = int(ms_str_send)
	ms_int_recv = int(ms_str_recv)
	print "number: "+str(package_num)
	print "Send Time: " + data,"from",addr
	print "Recv time: " + str(t)
	print ms_str_send + " " + ms_str_recv
	if(ms_int_recv<ms_int_send):
		ms_int_recv += 1000
	delaytime = ms_int_recv - ms_int_send
#	if delaytime <= 0:
#		delaytime = 1
	delay.append(delaytime)
	sum_delay += delaytime
	print delaytime
	print "\n"

	time.sleep(SEND_INTERVAL_TIME)
#print sumttl

	

	
for i in delay:
	print i
print "\n"
if (PACKAGES_NUMBER - miss_package)>0:
	print "connection: 1"
else:
	print "connection: 0"
recv_package = PACKAGES_NUMBER - miss_package
average_delay = float(sum_delay)/recv_package
print "Average Delay Time: "+str(average_delay)
sum_squares = 0.0
for i in delay:
	sum_squares += (i-average_delay)**2
#print sum_squares
delay_variation = math.sqrt(sum_squares/recv_package)
print "Packet Delay Variation: "+str(delay_variation)
print "Send Packages: " + str(PACKAGES_NUMBER)
print "Receve Packages: " + str(recv_package)
print "Miss Packages: " + str(miss_package)

