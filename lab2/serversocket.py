#!/usr/bin/env python

#Copyright (c) Cheng Chen

import socket, os, sys

#connect to IP and TCP
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#0.0.0.0 listens on all the ip address
serverSocket.bind(("0.0.0.0", 12345))

serverSocket.listen(5)

while True:
	print "Waiting for connection..."
	(clientSocket, address) = serverSocket.accept()
	print "We got a connetcion from %s" % (str(address))

#fork the process
	pid=os.fork()
	if (pid==0):
		#we must be in the child process
		request = bytearray()
		while True:
			part = clientSocket.recv(1024)
			if (part):
				request.extend(part)
				clientSocket.sendall(part)
			else:
				break

		print request
		sys.exit(0)
	else:
		#we must be in the parent process
		pass
