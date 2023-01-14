import time
import numpy as np
arr=np.array([1,0,3])

#copy array:-

#method 1:
copy_arr=arr.copy()
print(copy_arr)
copy_arr[1]=2  #chnaged element i copy array
print(arr)      #element of original array not going to change
print(copy_arr)

#method 2: (view method)
arr_v=arr.view()
print(arr_v)
arr_v[1]=5
arr[2]=6
print(arr)     #element of both array gets changed if we chnage element of any one array..
print(arr_v)

#method 3:
x=arr
print(x)
x[0]=4
print(x)   #element of both array gets changed if we chnage element of any one array..
print(arr)

print()

#creating range:-
arr=np.arange(10)
print(arr)
arr_2d=arr.reshape(2,5)

#Iterations:-
for i in arr_2d:
    print(i)     #i for each row
    time.sleep(1)

for row in arr_2d:
    for element in row:
        print(element)
        

#converting n-d into 1-d array and then print element:
for i in np.nditer(arr_2d):
    print(i)

for idx,i in np.ndenumerate(arr_2d):
    print(idx,i)


