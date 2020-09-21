#!/usr/bin/env python
import sys
import socket
import time

rhost=sys.argv[1]
rport = 1337
num = 0

while 1:
        try:
                s = socket.socket()
                s.connect((rhost,rport))
                if (port == 9765):
                        break
                newPort = newPort
                request = "GET / HTTP/1.1\r\nHost:%s\r\n\r\n" % rhost
                s.send(request.encode())
                response = s.recv(4096)
                httpResponse = repr(response)
                httpTrim = httpResponse[167:]
                httpTrim = httpTrim.replace('\'','')
                data = list(httpTrim.split(" "))
                port = int(data[2])
                print('Operation: '+data[0]+', number: '+ data[1]+', next port: '+ data[2]) 
                if(port != newPort):
                        if(data[0] == 'add'):
                                num += float(data[1])
                        elif(data[0] == 'minus'):
                                num -= float(data[1])
                        elif(data[0] == 'multiply'):
                                num *= float(data[1])
                        elif(data[0] == 'divide'):
                                num /= float(data[1])
                s.close()
        except:
                s.close()
                pass
print(num)
