
#calculator
def addition(x,y,a=4): #3a=4 is default argument should be written at end and can be rewrite in calling
    add=x+y
    return add
def subs(x,y):
    diff=x-y
    return diff
def mul(x,y):
    prod=x*y
    return prod
#[p*(p+q)]*[pq]=
p=int(input("Enter first number(p):"))
q=int(input("Enter first number(q):"))
res=mul(x=(mul(p,addition(p,q))),y=subs(p,q)) #passing arguments by mentioning actual name(x=p,y=q)=keyword arguments and it should for all arguments or only last argument
print("Result:",res)

#for loop with undefined numbers of arguments (arbitary arguments)(posional)
def mult(*num):
    prod=1
    for i in num:
        prod=prod*i
    return prod
print(mult(5,2,3))
