# Socket-Programming

## Work in progress!!

In this repository are developed (in Python) some simple computer networking concepts, in particular:
- a **Web Server** that will 
  1. create a connection socket when contacted by a client (browser), 
  2. reveive the HTTP request from this connection,
  3. parse the request to determine what file is requested,
  4. get the requested file from the server's file system, 
  send the response over the TCP connection to the requesting browser
- a **UDP Pinger** to estimate the delay (RTT) in a network
- a **Mail Client** that sends e-mails to any recipient by creating a TCP connection with a mail server, dialogue with it using the SMTP protocol and send an e-mail to a recipient.
- a **Web Proxi** that recieves an HTTP request for an object, generates a new HTTP reuest for the same object and sends it back to the origin server.

These programs where inspired by the classic "Computer Networking, A Top-Down Approach" by J. F. Kurose and K. W. Ross.
