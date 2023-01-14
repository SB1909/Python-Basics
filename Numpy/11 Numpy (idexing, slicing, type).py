import numpy as np
arr=np.array(range(10))   #or arr=np.arange(10)
#1-D
print(arr)
print(arr.ndim)
print()
#2-D
arr_2d=arr.reshape(2,5)
print(arr_2d)
print(arr_2d.ndim)
print()
#3-D
arr_3d1=arr.reshape(1,2,5)   #(depth,rows,columns)
print(arr_3d1)
print(arr_3d1.ndim)
print()
#3-D
arr=np.array(range(20))
arr_3d2=arr.reshape(2,2,5)
print(arr_3d2)
print(arr_3d2.ndim)
print()

#indexing:
print(arr[0])
print(arr_2d[0])
print(arr_2d[0][0])
print(arr_3d2[0])
print(arr_3d2[0][0][0])

#slicing:
print(arr[0:5])
print(arr_3d2[0:2])

#type:
print(arr.dtype)
print(type(arr))
arr=np.array([1,2.54])
print(arr.dtype)

#converting type:
new=arr.astype('i')  #float to int
print(new)
print(new.dtype)

New=arr.astype(bool)  #float to boolean
print(New)
print(New.dtype)

arr_2d=np.array([[2,3],[4,5],[6,7]])
print(arr_2d[0:2])    #[row range]
print(arr_2d[0:3,0])   #[row range:column range]
print(arr_2d[0,1])      #[row position,column position]
print(arr_2d[1,-2])  #row position==1,column element==-2: (4,5,4,5),(-2,-1,0,1)



