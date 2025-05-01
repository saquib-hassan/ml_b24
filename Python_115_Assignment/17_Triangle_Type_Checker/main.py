# Write a Python program that takes three sides of a triangle as input and determines whether it forms an equilateral, 
# isosceles, or scalene triangle.

a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

if a + b > c and a + c > b and b + c > a: #triangle inequality rule
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("This side doesn't form a valid triangle")
