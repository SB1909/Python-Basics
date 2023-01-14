import numpy as np
'''
a=np.array([[2],[3],[4]])
b=np.array([[1],[0],[1]])
c=np.array([[3],[8],[9]])

res=((2*a)+(8*b))+(3*(22+(6*c)))
print(res)
print(res.shape)


r1=(a.T@b) #result is scalar
res1=r1*c #result is vector
print(res1)
print(res1.shape)                          
r2=(b.T@c)
res2=a*r2
print(res2)
print(res2.shape)
#if (res1==res2).all(): OR
if np.array_equal(res1,res2):
    print("Associative")
else:
    print("Not Associative")

'''
a=np.array([[1],[0],[0],[1]])
b=np.array([[1],[1],[1],[1]])
c=np.array([[2],[3],[2],[3]])
#1st prb
res1=a+2*b+3*c
ind1=res1-res1 #for addition
inv1=res1*(-1)
print("ans1:",res1)
print(res1.shape)
print("identity1:",ind1)
print("inverse1:",inv1)
#2nd prb
res2=a*(c.T@b)*(2*a+3*b+2*c)
ind2=res2-res2
inv2=res2*(-1)
print("ans2:",res2)
print(res2.shape)
print("identity:",ind2)
print("inverse2:",inv2)
