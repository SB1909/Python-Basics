import socket
import time
myIP="127.0.0.1"
myPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM) #iv4,UDP
    print("Socket object s got created...")
    s.bind((myIP,myPort))     #binding ip and port
    print("Socket got binded...")
except:
    print("Please check your socket..")

while 4>2:
    data=s.recvfrom(100)
    time.sleep(2)
    print(data)
    rply=input("Enter your response:")
    rply_new=rply.encode('ascii')
    s.sendto(rply_new,data[1])
    print("Response send..")
s.close()
    
