lines_list=[]

# with open("sample.txt","r") as file:
#     lines_list=file.readlines()
with open("sample.txt","r") as file:
    for line in file:
        lines_list.append(line.strip())
print(lines_list)    