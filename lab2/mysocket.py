import socket
import sys
from thread import *

def clientthread(connection):
    while True:
        data = connection.recv(1024)

        if not data: 
            break
        stripped = data.strip("\r\n")	
     	connection.sendall(stripped + " Chen\r\n")
    connection.close()

#Create Server Socket
try:
    mysk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print("Failed to create socket")
    sys.exit();
print('Socket Created')
 
 #Bind to Port and IP
host = "localhost"
port = 8888

try:
	mysk.bind((host,port))
except:
	print("Failed to bind socket")
	sys.exit();
print('Bind Complete')

#Server Listens
mysk.listen(5)
print("Server is now listening")

#Keep connection open
while(True):
	connection, address = mysk.accept()
	start_new_thread(clientthread, (connection,))

mysk.close()
