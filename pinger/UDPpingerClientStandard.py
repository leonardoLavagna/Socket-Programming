# UDPPingerClient.py
from socket import *
import time
serverName = '64.233.167.99'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
receNum = 0
MaxDiffTime = -1
MinDiffTime = 2
AverDiffTime = 0
for i in range(10):
    time1 = time.time()
    outputdata = 'Ping ' + str(i) + " " + str(time1)
    clientSocket.settimeout(1)
    clientSocket.sendto(outputdata.encode(), (serverName, serverPort))
    try:
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
        timeDiff = time.time() - time1
        print(serverName, str(len(outputdata)), "RTT:", str(timeDiff))
        receNum += 1
        AverDiffTime += timeDiff
        if(timeDiff > MaxDiffTime):
            MaxDiffTime = timeDiff
        if (timeDiff < MinDiffTime):
            MinDiffTime = timeDiff
    except:
        print("Timeout")
print(serverName, "Ping:")
print(str(receNum), str(10-receNum), "(", str(int((10-receNum)*100/receNum)), "%)" )
if(receNum != 0):
    print(" estimated time: (min,max,avg)")
    print(MinDiffTime, MaxDiffTime, AverDiffTime/receNum)
