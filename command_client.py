#!/usr/bin/python2

import socket                   # Import socket module
from time import sleep

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.10.218"
port=8888

while True:
	cmd=raw_input("Please Type Command: ")
	s.sendto(cmd,(ip,port))
	sleep(2)
	t=s.recvfrom(100)
	print t[0]
