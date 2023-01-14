print("Select Operation")
print("+:Add,\n-:Subtract,\n*:Multiply,\n/:Divide")
while True:
    o=input("Enter Selected Operation(+,-,*,/): ")
    x=float(input("Enter Value of 1st number"))
    y=float(input("Enter Value of 2nd number"))
    if o=='+':
        print(x,"+",y,"=",x+y)
    elif o=='-':
        print(x,"-",y,"=",x-y)
    elif o=='*':
        print(x,"*",y,"=",x*y)
    elif o=='/':
        print(x,"/",y,"=",x/y)
    next_step=input("Want to do Next Calcuation? (Yes/No): ")
    if next_step=="No":
        break
else:
    print("Invalid Input")
    
