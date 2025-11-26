import math
a=float(input("enter the vakue for a:"))
b=float(input("enter the value for b:"))
c=float(input("enter the value for c:"))

d=(b**2)-(4*a*c)
if d>0:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print(f"the roots are real and different:\nroot1={root1}\nroot2={root2}")