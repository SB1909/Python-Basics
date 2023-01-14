'''
#function with fix arguments:
def mydata(name,gender="Male"):
    print(name,gender)
    return
mydata(name=input("Enter Name:"))
'''
'''
#function by value or by reference:
def passbyvalue(data):
    data.append([1,2,3,4])
    print("My value is",data)
    return
data=[10,20,30]
passbyvalue(data)
'''
'''
#variable length argument:
def myfunction(*x):
    print(x)
    print(type(x))
    return
myfunction(100,56,'hello')
'''
'''
#in form of dictionary:
def lnb(**learner):
    print("My name is",learner['fname'])
    print("Roll Number is",learner['rollnum'])
    return
lnb(fname="SB",rollnum="LnB001")
'''
'''
def square(x):
    return x**2 #square of variable
print(square(2))
print(square(4))

def cube(x):
    return x**3 #cube of variable
print(cube(2))
print(cube(8))
'''
'''
#function without any name:[lambda/anomy funtion]
cube=lambda x:x**3
print(cube(7))
'''

#recursion:[calling function automatically)
def recursion(k):
    if k>0:
        res=k+recursion(k-1) #[for k=3: res=3+(2-1)+(3-1)==6]
        print(res)
    else:
        res=0
    return res
recursion(int(input("Enter value:")))



