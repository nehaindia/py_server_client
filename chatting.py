#!/usr/bin/python2

#send Socket Creation

import socket,time


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)



ip="192.168.10.218"
port=8888

#while True:

	
#s.sendto("hello",(ip,port))
#	time.sleep(2)
#	print  s.recvfrom(100)


while True:

	message = raw_input("Client : ")
	s.sendto(message,(ip,port))
	t= s.recvfrom(1000)
	print "Receive from Server: " +t[0]
	
