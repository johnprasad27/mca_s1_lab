# 1 find positive number from list
numbers = [int(input("Enter number: ")) for _ in range(6)]

positive_numbers = [n for n in numbers if n > 0]
print(positive_numbers)

#square of numbers
numbers = [int(input("Enter number to be squared: ")) for _ in range(6)]

squares = [n*n for n in numbers]
print(squares)


#vowels in word

vowels = ['a','e','i','o','u']
word = input("Enter the word: ")

vowels_in_word = [ch for ch in word if ch in vowels]
print(vowels_in_word)


#ordinal list
word = input("Enter the string: ")

ordinal = [ord(ch) for ch in word]
print(ordinal)
   