x=int(input("Enter 1st Number"))
y=int(input("Enter 2nd Number"))
f=x+y
if (f>=10):
    print("Condition is Not Satisfy")
while True:
    x=int(input("Enter 1st Number"))
    y=int(input("Enter 2nd Number"))
    f=x+y
    if (f>=10):
        print("Condition is Not Satisfy")
    else:
        print("condition is satisfy")
    z=input("Enter Q to Stop")
    if (z=="Q"):
        break
    elif(z==" "):
        print("Loop will continue enter correct no")
        continue
    
