import socket
import random
from socket import *

#Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets 
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket 
seport = input("please enter serverPort number: ")
serverSocket.bind(('', seport))
print "The server is ready to receive"
while True:
    # Generate random number in the range of 0 to 10 
    rand = random.randint(0, 10)
    # Receive the client packet along with the address it is coming from 
    message, address = serverSocket.recvfrom(1024)
    # Capitalize the message from the client 
    message = message.upper()
    # If rand is less is than 2, we consider the packet lost and do not respond 
    if rand < 2:
        continue
    # Otherwise, the server responds 
    serverSocket.sendto(message, address)