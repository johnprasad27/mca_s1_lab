numbers=[]
n=int(input("enter the limits you want"))
for i in range(n):
    num=int(input("enter your number"))
    if num<100:
        numbers.append(num)
    else:
        numbers.append('over')
print(numbers)            