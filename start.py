#!/usr/bin/python2

#send Socket Creation

import socket,time


s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

from time import sleep

ip="192.168.10.218"
port=8888

print "**********************************************************************************"
print "*************************CHAT APPLICATIONS****************************************"
print "**********************************************************************************"
options='''
Press 1 to chat 
Press 2 to run command
Press 3 to file send
'''

print options

print "**********************************************************************************"

choice=raw_input() #for taking input from user

if choice == '1':
	s.sendto("1",(ip,port))
	execfile('chatting.py')
	time.sleep(2)
	
elif choice == '2':
	s.sendto("2",(ip,port))
	execfile('command_client.py')
	time.sleep(2)
	
	
elif choice == '3':
	s.sendto("3",(ip,port))
	execfile('send_file.py')
	time.sleep(2)
	
elif choice == 'q':
	exit()
else :
	print "Incorrect Choice"
	exit()

