import numpy as np

def vector():
    a=[int(input("Enter element in a vector ("+str(i+1)+"):"))for i in range(int(input("Enter number of elements in a vector (n):")))]
    return a

def vec_cal(a,b,c):
    print("\nSum of vectors (a+b+c):",a+b+c)
    print()
    
    vec_prd1=(a.T@b)*c
    print("Dot product of vectors((a@b)*c):",vec_prd1)
    vec_prd2=a*(b.T@c)
    print("Dot product of vectors(a*(b@c)):",vec_prd2)
    if (vec_prd1==vec_prd2).all():
        print("Associative for multiplication")
    else:
        print("Non associative for multiplication")
    print()
    
    for i in (a,b,c):
        print("Euclidean norm of vector",i,":",round(np.linalg.norm(i,2),3))
    print()
    
    for i in (a,b,c):
        print("Manhattan norm of vector",i,":",np.linalg.norm(i,1))
    print()
    
    for i in (a,b,c):
        print("Max norm of vector",i,":",np.linalg.norm(i,np.inf))
    print()

    for i in (a,b,c):
        print("Indentity of vector",i,":",i-i)
    print()
    
    for i in (a,b,c):
        print("Inverse of vector",i,":",i*(-1))
    print()
    
    euc_norm1=np.linalg.norm(a,2)
    euc_norm2=np.linalg.norm(b,2)
    euc_norm3=np.linalg.norm(c,2)
    
    theta1=(np.arccos((a.T@b)/(euc_norm1*euc_norm2)))
    print("Angle between vector a & b:",np.round(theta1*(180/np.pi),3))
    
    theta2=(np.arccos((b.T@c)/(euc_norm2*euc_norm3)))
    print("Angle between vector b & c:",np.round(theta2*(180/np.pi),3))
    
    theta3=(np.arccos((a.T@c)/(euc_norm1*euc_norm3)))
    print("Angle between vector a & c:",np.round(theta3*(180/np.pi),3))
    
    if theta1==0:
        print("True,vectors a & b are orthogonal")
    elif theta2==0:
        print("True,vectors b & c are orthogonal")
    elif theta3==0:
        print("True,vectors a & c are orthogonal")
    else:
        print("False, None of the vectors are orthogonal")     
    return

x=np.array(vector())
print("Vector1:\n",x)
y=np.array(vector())
print("Vector2:\n",y)
z=np.array(vector())
print("Vector3:\n",z)

vec_cal(x,y,z)

