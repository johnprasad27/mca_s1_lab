names=[]
for i in range(3):
    name=input("enter the first name")
    names.append(name)
print(names)    
count=0
for name in names:
    for ch in name:
        if ch =='a':
            count+=1
print(count)            
