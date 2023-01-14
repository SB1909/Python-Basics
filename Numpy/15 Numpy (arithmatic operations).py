import numpy as np

arr=np.arange(9,dtype=np.float_).reshape(3,3)
print(arr)

x=np.array([10,10,10])
y=np.array([10,11,12])

#addition:
print(arr+10)
print(arr+x)
print(np.add(arr,y))

#subtraction:
print(arr-y)
new=np.subtract(arr,y).astype('i')
print(new)

#multiply:
print(x*3)    #scalar multiplication
print(arr*x)  #matrix and vect multiply == mat
print(arr@x)  #dot prodct of mat and vec == vec

#divide:
print(np.divide(arr,2))

#exponent:
print(x**2)
print(x**[2,3,4])  #corresponding element
print(np.power(x,2))

#reciprocal:  (inverse)
a=np.array([0.25,1.2,0])  #for 0===inf
print(np.reciprocal(a))

#transpose:    column to row
arr_2d=np.array([[1,2,3,4],[5,6,7,8]])
print(arr_2d.T)

#identity:
print(np.identity(3))
print(np.identity(3,dtype='int'))
print(np.eye(3,3,0))

#maximum:
print(np.amax(arr))
print(np.amax(arr,0))  # 0 for in each column
print(np.max(arr,1))   # 1 for in each row

#minimum
print(np.amin(arr))
print(np.amin(arr,0))
print(np.min(arr,1))

#mean:
print(np.mean(arr))

#median:
print(np.median(arr))
