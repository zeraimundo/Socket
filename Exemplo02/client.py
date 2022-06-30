import time
from socket import *

pings = 1

while pings < 11:  

    clientSocket = socket(AF_INET, SOCK_DGRAM)

    clientSocket.settimeout(1)
    test = 'teste'
    message = bytes(test, encoding='utf8')

    addr = ("127.0.0.1", 12000)

    start = time.time()
    clientSocket.sendto(message, addr)

    try:
        data, server = clientSocket.recvfrom(1024)
        end = time.time()
        elapsed = end - start
        print( data )  
        print( pings)       
        print( elapsed )       
     

    except timeout:
        print ('REQUEST TIMED OUT')

    pings = pings - 1