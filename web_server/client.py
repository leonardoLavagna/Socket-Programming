from socket import *

# Get server host IP address and port number
serverIP = input("\n\nEnter the IP Address of the host : ")

# In the server side the port number is 6789
serverPort = int(input("Enter the port to connect to : "))

# Create socket
clientSocket = socket(AF_INET, SOCK_STREAM)

try:
    # Try connecting to the provided host
    clientSocket.connect((serverIP, serverPort))
    print("\nConnection Successful!")

    # Get the filename
    filename = input("\n\nEnter the relative path of the file to be retrieved : ")
    
    # Send the HTTP request message
    clientSocket.sendto(filename.encode(),(serverIP, serverPort))
    
    print("\n\n---------------HTTP RESPONSE---------------\n")

    # Receive one HTTP response header line
    response = clientSocket.recv(1024)
    print(response)

    # Receive the file
    fileData = clientSocket.recv(10000)
    print(fileData)

    print("---------------END OF HTTP RESPONSE---------------\n")

    # Close the connection
    clientSocket.close()

except error:
    print("\n\nError while connecting!")
    clientSocket.close()
