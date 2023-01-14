import math

def function(x):
    f1=round(math.cos(2*x))
    print("f(x):",f1)
    f2=round(2*(math.sin(2*x)))   #getting wrong value of sin(2x)==0
    print("f'(x):",f2)
    f3=round(4*math.cos(2*x))
    print('f"(x):',f3)
    return
function(math.pi)
