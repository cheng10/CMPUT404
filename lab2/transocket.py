#!/usr/bin/env python

#Copyright (c) Cheng Chen

import socket, os, sys, select

#connect to IP and TCP
serverSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

#0.0.0.0 listens on all the ip address
serverSocket.bind(("0.0.0.0", 12344))

serverSocket.listen(5)

while True:
	print "Waiting for connection..."
	(incomingSocket, address) = serverSocket.accept()
	print "We got a connetcion from %s" % (str(address))

#fork the process
	pid=os.fork()
	if (pid==0):
		#we must be in the child process
		outgoingSocket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		outgoingSocket.connect(("www.google.com", 80))
		request = bytearray()
		while True:
			incomingSocket.setblocking(0)
			try:
				part = incomingSocket.recv(1024)
			except socket.error as exception:
				if exception.errno == 11:
					part = None
				else:
					raise
			if (part):
				request.extend(part)
				outgoingSocket.sendall(part)
			#else:
			#	break
			outgoingSocket.setblocking(0)
			try:
				part = outgoingSocket.recv(1024)
			except socket.error as exception:
				if exception.errno == 11:
					part = None
				else:
					raise
			if (part):
				incomingSocket.sendall(part)
			select.select(
					[incomingSocket, outgoingSocket],
					[],
					[incomingSocket, outgoingSocket],
					1)
			#else:
			#	break
			
		print request
		sys.exit(0)
	else:
		#we must be in the parent process
		pass
