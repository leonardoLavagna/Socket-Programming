# Socket-Programming

In this repository are developed (in Python) some simple computer networking concepts, in particular:
- a **Web Server** that will 
  1. create a connection socket when contacted by a client (browser), 
  2. reveive the HTTP request from this connection,
  3. parse the request to determine what file is requested,
  4. get the requested file from the server's file system, 
  send the response over the TCP connection to the requesting browser
- a **UDP Pinger** to estimate the delay (RTT) in a network
- a **Mail Client** that sends e-mails to any recipient by creating a TCP connection with a mail server, dialogue with it using the SMTP protocol and send an e-mail to a recipient.
- a **Web Proxy** that recieves an HTTP request for an object, generates a new HTTP request for the same object and sends it back to the origin server.

### What's in here?
- A folder `web_server` with inside 4 files: the instructions `instructions.pdf`, a toy website `hello.html` and 2 python scripts to set up a web server to handle HTTP request over a TCP connection
- A folder `mail_service` with inside 3 python scripts to set up a mail client that dialogues with a mail server over a TCP connection using the SMTP protocol
- A folder `pinger` with inside 4 python scripts to build a pinger over a UDP connection, and an instructions' file
- A folder `proxy_server` with an instructions' file and a python script to create a web proxy that can recieve and respond to HTTP requests.

### Disclamair
These programs where inspired by the classic "Computer Networking, A Top-Down Approach" by J. F. Kurose and K. W. Ross.
