import numpy as np
x=np.array([8,10,11,-4,8])
y=np.array([-3,2,0,-4,11])
inner_product=np.dot(x,y) #dot product
print("Inner product of x,y:",inner_product)
euc_x=np.linalg.norm(x,2)
euc_y=np.linalg.norm(y,2)
print("Length of x:",euc_x)
print("Length of y:",euc_y)
dist=np.linalg.norm(x-y) #Euclidean Distance
print("Distance:",dist)
