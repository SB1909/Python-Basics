import numpy as np

a=np.matrix('1,2;3,4')   #in the form of string
print(a)
print(type(a))

b=np.matrix([[1,5],[6,6]])  #simple way of matrix
mat1=np.matrix('1,2,3,4;5,6,7,8;9,10,11,12;13,14,15,16')
print(mat1)
print(mat1.ndim)
print(mat1.size)  #no. of elements
print(mat1.real) #real number in matrix
mat2=mat1.T
print(mat2)
print(mat2.base) #for original matrix


#arithmatic operations:
print(np.add(mat1,mat2))
print(np.subtract(mat1,mat2))
print(np.divide(mat1,mat2))
print(np.sqrt(mat1))  #square root
print(np.sum(mat1))  #sum of all element
print(np.sum(mat1,axis=1)) #row wise addition of column elements
print(np.sum(mat1,axis=0)) # column wise addition of row elements

print(mat1==mat2)  #element wise true or false
print(mat1.argmax())  #max position in matrix
print(mat1.argmin())  #min position in matrix

#clip:
print(np.clip(mat1,3,10))    #(matrix,element <= n will be n, element >=n will be n)

#compress:
print(np.compress([0,1,1,0],mat1,axis=0))   #(0-eliminate/1-print(sequence=position),maxtrix,axis)

mat3=mat2.copy()   #copy

print(mat3.fill(0)) #all element will be n


#cummulative product:
print(np.cumprod(mat1,axis=1))    #product of all previous element: if axis=1, product of all column element row wise
print(np.cumprod(mat1,axis=0))  
print(np.cumsum(mat2))   #summation of all previous element printed in one row

print(mat1.diagonal())  #diagonal element

print(np.flipud(mat1))  #row interchanged== reverse order
print(np.fliplr(mat1))  #column interchange== reverse order

#indexing:
print(mat1[2,3])     #2,3 position
print(mat1[1:])      # 1st row to last row
print(mat1[1:,2:])   # 1st row to last, 2nd column to last

print(mat1.max(1))   # whole column which include max value  1=column / 0=row
print(mat1.min(0))   #min value row or column

#normal product:
print(mat1.prod(1))  #product of all column element
print(mat1.prod(0))  #product of all row element

print(mat1.nonzero())  #gives position of nonzero element in matrix

#repeating element:
from numpy import matrix as mxt
arr=mxt([1,2,3])
r=2
print(mxt.repeat(arr,r))








