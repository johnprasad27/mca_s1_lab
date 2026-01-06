# lambda functions
area_square = lambda a: a * a
area_rectangle = lambda l, b: l * b
area_triangle = lambda b, h: 0.5 * b * h

# input from user
side = float(input("Enter side of square: "))
length = float(input("Enter length of rectangle: "))
breadth = float(input("Enter breadth of rectangle: "))
base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))

# display results
print("Area of square:", area_square(side))
print("Area of rectangle:", area_rectangle(length, breadth))
print("Area of triangle:", area_triangle(base, height))
