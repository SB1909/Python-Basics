import numpy as np
x=([1,8,3])
y=([5,3,4])
numerator=np.dot(x,y)
L2x=np.linalg.norm(x,2)
L2y=np.linalg.norm(y,2)
cos_theta=numerator/(L2x*L2y)
print("cos_theta:",cos_theta)
theta=np.arccos(cos_theta) # cos inverse
print("Angle in radian:",theta)
Angle=theta*(180/np.pi)  #in degree conversion
print("Angle between x and y:",Angle)
