import numpy as np
print([i for i in dir(np) if 'rand' in i])

from numpy import random

#random num from 0 to 99 integer:
x=random.randint(100)
print(x)

#random 2-D array of given size integer:
x=random.randint(100,size=(3,3))
print(x)

#random number from 0 to 1 float:
x=random.rand()
print(x)

#random numbers from 0 to 1, count=given float:
x=random.rand(3)
print(x)

#from given list any random element:  #eqaul probability of getting selected
x=random.choice([3,5,6,8])
print(x)

#from given list any random element: (p=% of selection given)  (data distribution)
x=random.choice([3,5,7,9],p=[0.15,0.6,0.25,0])
print(x)

x=random.choice([3,5,7,9],p=[0.15,0.6,0.25,0],size=(2,2))
print(x)

#permutation of element (order of element gets changed):

#1] original array will not change:
arr=np.array([1,2,3,4])
x=random.permutation(arr)
print(arr)
print(x)

#2] original array will be change:
arr=np.array([1,2,3,4])
random.shuffle(arr)
print(arr)

