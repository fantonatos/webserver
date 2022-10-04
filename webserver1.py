# import socket module
from socket import *

# In order to terminate the program
import sys

# Prepare a sever socket
serverSocket = socket(AF_INET, SOCK_STREAM)
### YOUR CODE HERE ###

while True:
    # Establish the connection
    print('Ready to serve...')

    connectionSocket, addr = ### YOUR CODE HERE ###

    try:
        message = ### YOUR CODE HERE ###

        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = ### YOUR CODE HERE ###

        # Send one HTTP header line into socket
        ### YOUR CODE HERE ###

        # Send the content of the requested file into socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())

        # Close client socket
        connectionSocket.close()
    except IOError:
        # Send response message for file not found
        ### YOUR CODE HERE ###

        # Close client socket
        ### YOUR CODE HERE ###

# Close server socket
serverSocket.close()

# Terminate the program after sending the corresponding data
sys.exit()

