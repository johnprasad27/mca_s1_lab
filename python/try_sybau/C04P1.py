class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        area=self.breadth*self.length 
        return(area)

r1=Rectangle(1,2)
r2=Rectangle(3,4)  
ar1=r1.area()
ar2=r2.area()   
if ar1>ar2:
    print("first rectangle is bigger with area",ar1) 
else:
     print("second rectangle is bigger with area",ar2) 
    
