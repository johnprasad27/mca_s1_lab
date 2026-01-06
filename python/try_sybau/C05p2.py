lines_list=[]
count=1
with open("sample.txt","r") as file:
    for line in file:
        if count%2==1:
            lines_list.append(line.strip())
        count+=1
print(lines_list)            