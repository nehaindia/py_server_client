#!/usr/bin/python2

#send Socket Creation

import socket


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


ip="192.168.10.218"
port= 8888

s.bind((ip,port))
while True :
	t= s.recvfrom(40)
	print "client option ::::: " + t[0]
	if t[0] == "1":
		print "client want to chat"
		execfile('sktrecv.py')
	elif t[0]== "2" :
		print "client want to run commands" 
		execfile('command_Server.py')
	elif t[0]=="3" :
		print "client want to send file"
		execfile('receive_file.py')
	else :
		exit()



	
	


 
