#!/usr/bin/python2

#send Socket Creation

import socket,sys


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



ip="192.168.10.218"
port=8888
TIMEOUT=10

s.settimeout(TIMEOUT)

#while True:

	
#s.sendto("hello",(ip,port))
#	time.sleep(2)
#	print  s.recvfrom(100)

try:
	while True:
		message = raw_input("Client : ")
		s.sendto(message,(ip,port))
		t= s.recvfrom(1000)
		print "Receive from Server: " +t[0]
		user=raw_input("Do you want to quit : Y/N")
		if user == 'Y' :
			s.sendto("Client has Quit : Please exit",(ip,port))
			exit()
except:
	print "Timeout or No client running"
	
