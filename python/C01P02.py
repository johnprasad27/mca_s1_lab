import math 
def switch(a,b):
    print(f"a=",a,"b=",b)
    a=a+b
    b=a-b
    a=a-b
    print(f"a=",a,"b=",b)
    return(a,b)
switch(8,3)