list1=[]
list2=[]

n=int(input("enter the length for list 1"))

for i in range(n):
    num=int(input("enter the number"))
    list1.append(num)

n=int(input("enter the length for list 2"))    
for i in range(n):
    num=int(input("enter the number"))
    list2.append(num)

if len(list1)==len(list2):
    print("same length")

if sum(list1)==sum(list2):
    print(" is same sum",sum(list1))
for item in list1:
    if item in list2:
        print("same value",item)