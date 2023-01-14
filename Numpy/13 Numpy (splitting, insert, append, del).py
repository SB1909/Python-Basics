import numpy as np
arr=np.arange(1,10)
print(arr)

#spliting array
x=np.split(arr,3)  #3== element in each row (equally split)
print(x)

y=np.array_split(arr,4)   #4== no of array
print(y)

#Insert:
a=np.array([[1,1],[2,2],[3,3]])
print(a)
p=np.insert(a,1,5,axis=1)     #for column axis=1   and for row axis=0
print(p)
p=np.insert(a,1,5,axis=0)     #(array,position,element,column/row)
print(p)

p=np.insert(a,1,[[4],[5],[6]],axis=1)  #inserting more than one column/row
print(p)

p=np.insert(a,[1],[[4],[5],[6]],axis=1)  #inserting different element in one column/row
print(p)


#append:
a=np.array([[1,1],[2,2],[3,3]])
b=np.append(a,[[4,4,4],[5,5,5],[6,6,6]],axis=1)     #(array,elements,axis)
print(b)
b=np.append(a,[[4,4]],axis=0)
print(b)


#delete:
x=np.arange(1,10).reshape(3,3)
print(x)
y=np.delete(x,1,0)  #(array,row,column)
print(y)
