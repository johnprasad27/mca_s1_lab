#frequency of each character in a string
string=input("enter a string:")
freq={}
for ch in string:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print("frequency of each character in a string is:",freq)