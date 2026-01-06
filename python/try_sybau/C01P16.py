s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

# swap character at position 1
new_s1 = s1[0] + s2[1] + s1[2:]
new_s2 = s2[0] + s1[1] + s2[2:]

result = new_s1 + " " + new_s2
print(result)
