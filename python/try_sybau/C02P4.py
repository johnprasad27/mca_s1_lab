import math

start = int(input("Enter starting range: "))
end = int(input("Enter ending range: "))

result = []

for num in range(start, end + 1):
    # check four-digit number
    if 1000 <= num <= 9999:
        
        # check all digits are even
        digits_even = True
        for d in str(num):
            if int(d) % 2 != 0:
                digits_even = False
                break
        
        # check perfect square
        root = int(math.sqrt(num))
        if digits_even and root * root == num:
            result.append(num)

print("Result:", result)
