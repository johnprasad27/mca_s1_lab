year = int(input("enter the year to which you wantleap year"))
print(year)

for y in range(2026,year):
 
 if((y%4==0 and y%100!=0) or (y%400==0)):
    print(y)