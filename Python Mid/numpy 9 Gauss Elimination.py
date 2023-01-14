import numpy as np
A=np.array([[1,3,5],[2,2,-1],[1,3,2]])
y=np.array([[-1],[1],[2]])
print(np.linalg.solve(A,y)) #gauss elimination

A=np.array([[4,3,-5],[-2,-4,5],[8,8,0]])
y=np.array([[2],[5],[-3]])
print(np.linalg.solve(A,y))
