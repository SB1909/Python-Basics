'''
x=int(input("Enter Value of x:"))
y=int(input("Enter Value of y:"))
'''

'''
#nested if
if x>y:
    print(x,"is greater than",y)
    if x>10:
        print(x,"is greater than 10")
    else:
        print(x,"is lesser than or equal to 10")
else:
    print(x,"is lesser than",y)
'''

'''
#and function
if x>10 and y<12:
   print("I am Okay") 
else:
    print("I am not Okay")
'''


#Dictionary
username_password={"lnb":123,"SB":234,"Data":345}
while True:
    user=input("Enter Username:")
    if user in username_password:
        print("User is Present")
        pw=int(input("Enter Password:"))
        if pw==username_password[user]:
            print("Password is Correct")
            break
        else:
            print("Password is Incorrect")
            next_step=input("Want to try again? (Yes/No):")
            if next_step=="No":
                break
    else:
        print("User is not present")

