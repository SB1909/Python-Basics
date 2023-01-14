import numpy as np
x=np.array([3,-4])
print(x.shape)
print(x.ndim) #dimenstions vector=1, matrix=2
L2=np.linalg.norm(x,2) #2 for euclidean norm
print("L2:",L2)
L1=np.linalg.norm(x,1) #1 for manhattan norm
print("L1:",L1)
L_infy=np.linalg.norm(x,np.inf) #np.inf for Max norm
print("L Infinity:",L_infy)
