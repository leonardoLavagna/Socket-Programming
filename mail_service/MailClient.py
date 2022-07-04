from socket import *
import base64

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = input("Enter mail server : ")
mailUser = input("Enter your mail.com username : ")
mailFromAddress = mailUser + '@'+ mailserver
mailPassWord = input("Enter your mail.com password : ")
mailToAddress = input("\nEnter the recipient's email address : ")

msg = 'FROM: ' + mailFromAddress + '\r\n'
msg += 'TO: ' + mailToAddress +  '\r\n'
msg += 'Subject: ' + 'test' +  '\r\n'
msg += "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with mailserver
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 25))

recv = clientSocket.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO mailserver\r\n'
while True:
    clientSocket.send(heloCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

loginCommand = 'auth login\r\n'
while True:
    clientSocket.send(loginCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
while True:
    clientSocket.send(userCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
while True:
    clientSocket.send(passCommand)
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '235':
        break

# Send MAIL FROM command and print server response.
MFCommand = 'MAIL FROM: <'+ mailFromAddress + '>\r\n'
while True:
    clientSocket.send(MFCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send RCPT TO command and print server response.
RTCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
while True:
    clientSocket.send(RTCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send DATA command and print server response.
DATACommand = 'DATA\r\n'
while True:
    clientSocket.send(DATACommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '354':
        break

# Send message data.
clientSocket.send(msg.encode())

# Message ends with a single period.
while True:
    clientSocket.send(endmsg.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send QUIT command and get server response.
QUITCommand = 'QUIT\r\n'
while True:
    clientSocket.send(QUITCommand.encode())
    recv = clientSocket.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '221':
        break
