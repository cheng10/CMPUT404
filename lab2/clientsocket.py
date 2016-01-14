#!/usr/bin/env python

#Copyright (c) Cheng Chen

import socket

#connect to IP and TCP
clientSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect to google
#c takes a struct, hence we have double paratheses here
clientSocket.connect(("www.google.com", 80))

request="GET / HTTP/1.0\n\n"

clientSocket.sendall(request)

response = bytearray()
done=False
while True:
	part = clientSocket.recv(1024)
	if (part):
		response.extend(part)
	else:
		break

print response
