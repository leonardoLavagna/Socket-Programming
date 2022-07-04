from socket import *
import base64
import ssl

# Choose a mail server (e.g. Google mail server) and call it mailserver
mailserver = input("Enter mail server : ")
mailUser = input("Enter your mail.com username : ")
mailFromAddress = mailUser + '@'+ mailserver
mailPassWord = input("Enter your mail.com password : ")
mailToAddress = input("\nEnter the recipient's email address : ")

# transfer image and html
with open("timg.jpg","rb") as f:
    image_data = base64.b64encode(f.read())
with open("hello.html","rb") as f:
    html_data = base64.b64encode(f.read())


msg = 'FROM: ' + mailFromAddress + '\r\n'
msg += 'TO: ' + mailToAddress +  '\r\n'
msg += 'Subject: ' + 'text and picture' +  '\r\n'
msg += 'Content-Type:multipart/related; boundary="----=_NextPart_000_0012345JZ"\r\n'
msg += 'MIME-Version: 1.0\r\n'
msg += '\r\n'
msg = msg.encode()
msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
msg += 'Content-Type: text/html; charset=UTF-8\r\n'.encode()
msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
msg += '\r\n'.encode()
msg += html_data
msg += '\r\n'.encode()
msg += '\r\n'.encode()
msg += '------=_NextPart_000_0012345JZ\r\n'.encode()
msg += 'Content-Type: image/jpeg; name="timg.jpg"\r\n'.encode()
msg += 'Content-Transfer-Encoding: base64\r\n'.encode()
msg += 'Content-ID: JZJZJZJZJZJZJZJZ'.encode()
msg += '\r\n'.encode()
msg += image_data + "\r\n".encode()
msg += '\r\n'.encode()
msg += '------=_NextPart_000_0012345JZ--\r\n'.encode()
endmsg = "\r\n.\r\n"

# Create socket called clientSocket and establish a TCP connection with mailserver
context = ssl.create_default_context()
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, 465))
clientSocketSSL = context.wrap_socket(clientSocket, server_hostname=mailserver)

recv = clientSocketSSL.recv(1024)
recv = recv.decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
heloCommand = 'HELO mailserver\r\n'
while True:
    clientSocketSSL.send(heloCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

loginCommand = 'auth login\r\n'
while True:
    clientSocketSSL.send(loginCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

userCommand = base64.b64encode(mailUser.encode()) + b'\r\n'
while True:
    clientSocketSSL.send(userCommand)
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '334':
        break

passCommand = base64.b64encode(mailPassWord.encode()) + b'\r\n'
while True:
    clientSocketSSL.send(passCommand)
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '235':
        break

# Send MAIL FROM command and print server response.
MFCommand = 'MAIL FROM: <'+ mailFromAddress + '>\r\n'
while True:
    clientSocketSSL.send(MFCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send RCPT TO command and print server response.
RTCommand = 'RCPT TO: <'+ mailToAddress + '>\r\n'
while True:
    clientSocketSSL.send(RTCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send DATA command and print server response.
DATACommand = 'DATA\r\n'
while True:
    clientSocketSSL.send(DATACommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '354':
        break

# Send message data.
clientSocketSSL.send(msg)

# Message ends with a single period.
while True:
    clientSocketSSL.send(endmsg.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '250':
        break

# Send QUIT command and get server response.
QUITCommand = 'QUIT\r\n'
while True:
    clientSocketSSL.send(QUITCommand.encode())
    recv = clientSocketSSL.recv(1024)
    recv = recv.decode()
    print(recv)
    if recv[:3] == '221':
        break

clientSocketSSL.close()
