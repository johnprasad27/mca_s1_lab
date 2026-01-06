words = []

n = int(input("How many words? "))

for i in range(n):
    word = input("Enter word: ")
    words.append(word)

max_len = 0

for word in words:
    if len(word) > max_len:
        max_len = len(word)

print("Length of longest word:", max_len)
