string = input("Enter your string: ")

result = string[0] + string[1:].replace(string[0], '$')
print(result)
