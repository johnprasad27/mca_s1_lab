def fact(num):
    if num==1:
        return 1
    else:
        print(num)
        return num*fact(num-1)

print(fact(5))   