from socket import *
import time

serverName = '127.0.0.1'
serverPort = 12000

# Creating an UDP socket for the client
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Setting the timeout to 1 second as required in the assignment
clientSocket.settimeout(1.0)

# Sending 10 pings
for seq in range(1, 11):
    sendTime = time.time()
    
    # Messaging format: Ping sequence_number time
    message = f"Ping {seq} {sendTime}"
    
    try:
        # Sending the packet to the server
        clientSocket.sendto(message.encode(), (serverName, serverPort))
        
        # Receive server response
        response, address = clientSocket.recvfrom(1024)
        
        # Calculating the RTT
        rtt = time.time() - sendTime
        
        # Print response and RTT
        print(f"Received {response.decode()} | RTT: {rtt} seconds")
        
    except timeout:
        # Print request timed out if no response within 1 second
        print(f"Ping {seq}: Request timed out")

# Close socket when done
clientSocket.close()