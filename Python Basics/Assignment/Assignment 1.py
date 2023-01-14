#Ans1:
'''
a=1
b=2
c=3
d=4
e=5
A=a+(((b/c)**d)*e)
print(A)
B=a+((b/(c**d))*e)
print(B)
C=(a+b/c)**(d*e)
print(C)
'''

#Ans2:
'''
T=1
F=0
#different values:
E1=T
E2=F
if not(E1 or E2)==(not E1 and not E2):
    print("True")
else:
    print("False")

#same values:
E1=T
E2=T
if not(E1 or E2)==(not E1 and not E2):
    print("True")
else:
    print("False")
'''

#Ans3:
'''
#slicing
word='abracadabra' #string type (a  r b a d a c a r b a b r a c a d a b r a)
print(word[3:7])            #  (-10-9-8-7-6-5-4-3-2-1 0 1 2 3 4 5 6 7 8 9 10)
print(word[4:8])
print(word[-4:-8])
print(word[-8:-4])
print(word[-1])
print(word[-8])
print(word[0])
print(word[-4])
'''

#Ans4:
'''
x=15%5//5*10**5
print(x)
print(type(x))
y="1+2+3"
print(y)
print(type(y))
z=10**10/5+25-50
print(z)
print(type(z))
a=9//3+3**3>3*3*3
print(a)
print(type(a))
b=50*100.0//10%5
print(b)
print(type(b))
'''

#Ans5:
'''
#(str+str)*int
a,b,c,d=input()
d=3
print((a+b+c)*d)
'''

#Ans6:
'''
L=[-1,1]
for i in range(8):
    size=len(L)
    value=L[size-2]+L[size-1]
    L.append(value)
print(L)
'''

#Ans7:
'''
def fun(a,b,c):
    for i in range(a,b,c):
        print(i)
print(fun(10,-1,-1))   #ans
print(fun(-10,1,1))    #ans
#print(fun(10,-2,-0))    
#print(fun(10,-2,1))
'''

#Ans8:
'''
def fun(word):
    if word.isalpha():
        word=word.lower()
        word=word+'12345'
    else:
        word='abcd'+word
    print(word)
    return
fun('abcd')     #abcd12345
fun('ABCD')     #abcd12345
fun('12345')    #abcd12345
fun('54321')
fun('abcd12345')
fun('dcba')
'''

#Ans9:
'''
def fun(limit):
    pi='3.1415926535'
    output=''
    index=0
    while len(output)<limit:
        output=output+pi[index]
        index=index+1
    print(output)
fun(2)
fun(3)
fun(4) #3.14
fun(5)
'''

#Ans10:
'''
n=int(input())
a=0
for i in range(1,n+1):
    b=1
    for j in range(1,i+1):
        b=b*j
    a=a+b
print(a)   #sum of factorial of the first n natural numbers
'''

#Ans11:
'''
L=[[1,2,3],['a','b','c'],'abc']
count=0
for elem in L:
    count=count+len(elem)
print(count)
'''

#Ans12:
'''
def f(L,m):
    L=L*m
    return L
x=[0]
y=2
print(type(f(x,y)))
print(f(x,y))
'''

#Ans13:
'''
def myprint(msg,num):
    output=''
    for i in range(num):
        output=output+msg
    return output
print(myprint('python',3))
'''

#Ans14:

#a (wrong)
def is_plane(L):
    for elem in L:
        a,b,c=elem[0],elem[1],elem[2]
        if (3*a)-(4*b)+(11*c)==0:
            return True       #returning value from here in first true pass
        else:
            return False
x=[[2,7,2],[2,7,3]]
print(is_plane(x))

#b
def is_plane(L):
    for elem in L:
        a,b,c=elem[0],elem[1],elem[2]
        if (3*a)-(4*b)+(11*c)!=0:     #!= : not equal to
            return False
    return True
x=[[2,7,2],[2,7,3]]
print(is_plane(x))

#c (wrong)
def is_plane(L):
    for elem in L:
        count=0     #every time count becomes 0, so lenght becomes 1
        a,b,c=elem[0],elem[1],elem[2]
        if (3*a)-(4*b)+(11*c)==0:
            count=count+1
    if count==len(L):
        return True
    return False
x=[[2,7,2,],[2,7,2]]
print(is_plane(x))

#d
def is_plane(L):
    count=0
    for elem in L:  
        a,b,c=elem[0],elem[1],elem[2]
        if (3*a)-(4*b)+(11*c)==0:
            count=count+1
    if count==len(L):
        return True
    return False
x=[[2,7,2],[2,7,3]]
print(is_plane(x))


