#!/usr/bin/python2

#send Socket Creation

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip="192.168.10.218"
port= 8888

s.bind((ip,port))

#while(4>2):
#	t= s.recvfrom(40)
#	print "rec from client" +t[0]
#	s.sendto("hello",t[1])


while True :


	r = s.recvfrom(1000)
	print "receive from client : " + r[0]
	reply = raw_input('server : ')
	client_address = r[1]
	s.sendto(reply, client_address)  
