import numpy as np

#adiition and substraction:
P=np.array([[1,2],[3,4],[5,6]])
Q=np.array([[2,3],[3,3],[1,1]])
print("P=",P)
print(P.shape)
print("Q=",Q)
print(Q.shape)
R1=P+Q
R2=P-Q
print("P+Q:","\n",R1)
print(R1.shape)
print("P-Q:",'\n',R2)
print(R2.shape)

#scalar multiplication:result=vector
a=3
R3=a*P
print("a*P=",a,"*P=","\n",R3)
print(R3.shape)


#multiplication with vector (Dot Product):result=vector
#column of matrix==rows of vector
A=([[1,2,3],[4,5,6],[7,8,9]])
x=([[2],[3],[4]])
print(A)
print(A.shape)
print(x)
print(x.shape)
#R5=A@x
R5=np.dot(A,x)
print("A.x=A@x=","\n",R5)


#multiplication of matrix vs matrix:
#(column of matrix==rows of vector)
P=np.array([[1,2,3],[3,4,5],[5,6,7]])
Q=np.array([[2,3],[3,3],[1,1]])
print("P=",P)
print(P.shape)
print("Q=",Q)
print(Q.shape)
#R6=np.dot(P,Q)
R6=P@Q
print("P.Q=P@Q=","\n",R6)
print(R6.shape) #result=rows(1st)xcolumn(2nd)
'''

#Inverse of matrix: (square matrix)
P=np.array([[1,0,1],[0,3,2],[4,3,5]]) #should be non-singular matrix...determinant should be zero
print("P=","\n",P)
print(P.shape)

#R7=np.linalg.inv(P)
R7=np.round(np.linalg.inv(P))
print("Inv(P):",'\n',R7)

#Identity Matrix: (diagonal=1, non-diagonal=0)
R8=np.round(P@R7)
print("Indetity(P):",'\n',R8)
print(R8.shape)

#Transpose:
R9=P.T
print("Transpose(P):",'\n',R9)
print(R9.shape)
'''


