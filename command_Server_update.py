#!/usr/bin/python2

import socket                   # Import socket module
import os
import sys
import subprocess 

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

ip="192.168.10.218"
port=8888
TIMEOUT=20


s.bind((ip,port))
s.settimeout(TIMEOUT)

try:
	while True:
		client = s.recvfrom(40)
		p = subprocess.Popen(client[0],stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
		(command,error)= p.communicate()
		return_code = p.returncode
		
		
		if p.returncode == 0:
			message=str(command)
			s.sendto(message,client[1])
		else :
			print str(error)
			message=str(error)
			s.sendto(message,client[1])

except OSError as e:
	message="COMMAND NOT FOUND"
	s.sendto(message,client[1])
	
except:
	print "timeout or no server running"
			

	


