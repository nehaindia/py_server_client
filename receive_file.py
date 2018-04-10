#!/usr/bin/python2

from socket import *
import sys
import select

host="192.168.10.218"
port = 9999
s = socket(AF_INET,SOCK_DGRAM)
s.bind((host,port))

addr = (host,port)
buf=1024


f = open("op.pdf",'wb')
data,addr = s.recvfrom(buf)


while(data):
    f.write(data)
    s.settimeout(2)
    data,addr = s.recvfrom(buf)

f.close()
s.close()
