line=input("enter your text")
words_list=line.split()
count={}

for word in words_list:
    if word in count:
        count[word]+=1
    else:
        count[word]=1
print(count)            