from socket import *
import sys

s = socket(AF_INET,SOCK_DGRAM)
host ="192.168.10.218"
port = 9999
buf =1024
addr = (host,port)

name_file= str(raw_input("Enter name of file u want to send"))
print name_file

f=open (name_file, "rb") 
data = f.read(buf)
while (data):
    if(s.sendto(data,addr)):
        print "sending ..."
        data = f.read(buf)
s.close()
f.close()
