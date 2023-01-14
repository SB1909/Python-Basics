import socket
import time
targetIP="127.0.0.1"
targetPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #iv4,UDP
    print("Socket object s got created...")
except:
    print("Please check your socket..")

while 3>2:
    msg=input("Enter your messege:")
    new_msg=msg.encode('ascii')
    s.sendto(new_msg,(targetIP,targetPort))
    print("Data sent...")
    print("waiting for their response...")
    print(s.recvfrom(100))
s.close()
    
