import numpy as np

#vector input:-
'''
def vector():
    a=[int(i)for i in input("Enter elements in a vector seperated by comma:").split(",")]
    #or
    a=[int(input("Enter element in a vector ("+str(i+1)+"):"))for i in range(int(input("Enter number of elements in a vector (n):")))]
    return a

#OR

def vector():
    n=int(input("Enter number of elements in a vector (n):"))
    a=[]
    for i in range(n):
        v=int(input("Enter Element ("+str(i+1)+"):"))
        a.append(v)
    return a

x=np.array(vector())
print("Vector1:\n",x)
'''



#Matrix inputs:-
'''
def matrix(): 
    m=[]
    row=int(input("Enter number of Rows of matrix:"))
    column=int(input("Enter number of columns of matrix:"))
    for i in range(row):
        a=[]
        for j in range(column):
            var=int(input("Enter element of matrix ("+str(i+1)+""+str(',')+""+str(j+1)+"):"))
            a.append(var)
        m.append(a)
    return m
'''
#OR

def matrix():
    r=int(input("Enter number of Rows of matrix:"))
    c=int(input("Enter number of columns of matrix:"))
    m=[[int(input("Enter element of matrix ("+str(i+1)+""+str(',')+""+str(j+1)+"):"))for j in range(c)]for i in range(r)]
    return m

m1=np.array(matrix())
print("Matrix 1:\n",m1)

