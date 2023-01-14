import math

def area_shape(shape):
    shape=shape.lower()
    if shape=='triangle':
        b=float(input("Enter base of the triangle (b):"))             
        h=float(input("Enter height of the triangle (h):"))
        area1=round(((1/2)*b*h),3)
        print("Area of the triangle is:",area1)
    elif shape=='circle':
        r=float(input("Enter radius of the circle (r):"))
        area2=round((math.pi*r**2),3)
        print("Area of the circle is:",area2)
    elif shape=='rectangle':
        l=float(input("Enter length of the rectangle (l):"))
        b=float(input("Enter breadth of the rectangle (b):"))
        area3=round((l*b),3)
        print("Area of the rectangle is:",area3)
    else:
        print("Invalid Input")
    return
area_shape(input("Enter name of shape:"))

#cylinder
def cylinder(r,h):
    area_cyl=round((2*math.pi*r*h)+(2*math.pi*r**2),3)
    print("Surface area of the Cylinder is:",area_cyl)
    vol=round(math.pi*r**2*h,3)
    print("Volume of the Cylinder is:",vol)
    return
cylinder(float(input("Enter the radius of cylinder (r):")),float(input("Enter the height of cylinder (h):")))
