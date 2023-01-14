import numpy as np

def matrix():
    r=int(input("Enter number of Rows of matrix:"))
    c=int(input("Enter number of columns of matrix:"))
    m=[[int(input("Enter element of matrix ("+str(i+1)+""+str(',')+""+str(j+1)+"):"))for j in range(c)]for i in range(r)]
    return m
print("Matrix 1:")
m1=np.array(matrix())
print(m1)
print()
print("Matrix 2:")
m2=np.array(matrix())
print(m2)
print()               
def calculation(x,y):
    return print("Summation:\n",np.round(x+y,2),"\nDifference:\n",np.round(x-y,2),"\nMultiplication:\n",np.round(np.dot(x,y),2),"\nDivision:\n",np.round(x/y,2))
calculation(m1,m2)
