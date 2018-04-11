#!/usr/bin/python2

#send Socket Creation

import socket,sys


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip="192.168.10.218"
port= 8888
TIMEOUT=10


s.bind((ip,port))
s.settimeout(TIMEOUT)

#while(4>2):
#	t= s.recvfrom(40)
#	print "rec from client" +t[0]
#	s.sendto("hello",t[1])

try :
	while True :
		r = s.recvfrom(1000)
		print "receive from client : " + r[0]
		reply = raw_input('server : ')
		client_address = r[1]
		s.sendto(reply, client_address)
except:
	print "timeout or no server running"
	
