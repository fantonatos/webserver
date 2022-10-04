#!/usr/bin/env python

# import socket module
from socket import *

# In order to terminate the program
import sys

# Prepare a sever socket
# open socket on port 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
serverSocket.bind(('', 8080))
serverSocket.listen(10)

while True:
    # Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = serverSocket.accept()

    try:
        message = connectionSocket.recv(1024).decode()

        filename = message.split()[1]

        f = open(filename[1:])

        # read entire file into outputdata
        outputdata = f.readlines()

        # Send one HTTP header line into socket
        connectionSocket.send('HTTP/1.1 200 OK\r\n'.encode())
        connectionSocket.send('\r\n'.encode())

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        connectionSocket.send('HTTP/1.1 404 NOT FOUND\r\n'.encode())


        # Close client socket
        connectionSocket.close()

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

