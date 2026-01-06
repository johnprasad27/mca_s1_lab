class Rectangle:
    def __init__(self,breadth,length):
        self.breadth=breadth
        self.length=length
    def area(self):
        area=self.breadth*self.length 
        return(area)
    def __gt__(self,other):
        return self.area()>other.area()

r1=Rectangle(1,2)
r2=Rectangle(3,4)  
  
if r1>r2:
    print("first rectangle is bigger with area",r1.area()) 
else:
     print("second rectangle is bigger with area",r2.area()) 
    