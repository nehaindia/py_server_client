#!/usr/bin/python2

import socket                   # Import socket module
from time import sleep
import sys

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.10.218"
port=8888
TIMEOUT=20
s.settimeout(TIMEOUT)

try:
	while True:
		cmd=raw_input("Please Type Command: ")
		s.sendto(cmd,(ip,port))
		sleep(2)
		t=s.recvfrom(100)
		print t[0]
		user=raw_input("Do you want to quit : Y/N")
		if user == 'Y' :
			s.sendto("Client has Quit : Please exit",(ip,port))
			exit()
except:
	print "Timeout or No client running"
