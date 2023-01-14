import numpy as np

def vector():
    a=[int(input("Enter element in a vector ("+str(i+1)+"):"))for i in range(int(input("Enter number of elements in a vector (n):")))]
    return a

def vec_cal(a,b,c):
    print("Ans1:","\nSum of vectors (a+b+c):\n",a+b+c)
    vec_prd1=(a.T@b)*c
    print()
    print("Ans2:","\nDot product of vectors((a@b)*c):\n",vec_prd1)
    vec_prd2=a*(b.T@c)
    print("Dot product of vectors(a*(b@c)):\n",vec_prd2)
    if (vec_prd1==vec_prd2).all():
        print("Associative for multiplication")
    else:
        print("Non associative for multiplication")
    print()
    euc_norm1=np.linalg.norm(a,2)
    print("Ans3:","\nEuclidean norm of vector a:",round(euc_norm1,3))
    euc_norm2=np.linalg.norm(b,2)
    print("Euclidean norm of vector b:",round(euc_norm2,3))
    euc_norm3=np.linalg.norm(c,2)
    print("Euclidean norm of vector c:",round(euc_norm3,3))
    print()
    manh_norm1=np.linalg.norm(a,1)
    print("Manhattan norm of vector a:",manh_norm1)
    manh_norm2=np.linalg.norm(b,1)
    print("Manhattan norm of vector b:",manh_norm2)
    manh_norm3=np.linalg.norm(c,1)
    print("Manhattan norm of vector c:",manh_norm3)
    print()
    max_norm1=np.linalg.norm(a,np.inf)
    print("Max norm of vector a:",max_norm1)
    max_norm2=np.linalg.norm(b,np.inf)
    print("Max norm of vector b:",max_norm2)
    max_norm3=np.linalg.norm(c,np.inf)
    print("Max norm of vector c:",max_norm3)
    print()
    print("Ans4:","\nIndentity of vector a:\n",a-a)
    print("Indentity of vector b:\n",b-b)
    print("Indentity of vector c:\n",c-c)
    print("Inverse of vector a:\n",a*(-1))
    print("Inverse of vector b:\n",b*(-1))
    print("Inverse of vector c:\n",c*(-1))
    print()
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
        print("Ans5:\n","False, None of the vectors are orthogonal")     
    return

x=np.array(vector())
print("Vector1:\n",x)
y=np.array(vector())
print("Vector2:\n",y)
z=np.array(vector())
print("Vector3:\n",z)

vec_cal(x,y,z)

