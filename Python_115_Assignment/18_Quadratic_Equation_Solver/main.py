# Write a Python program that takes the coefficients (a, b, c) of a quadratic equation as input and calculates and 
# prints the real roots (if they exist) or a message indicating the complex roots.

import math

#coefficients a, b, c
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

if a == 0:
    print("This is not a quadratic equation.")
else:
    discriminant = b**2 - 4*a*c # discriminant = b^2 - 4ac

    if discriminant > 0: # if discriminant >0 there're two distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two real and distinct roots:")
        print("Root 1 =", root1)
        print("Root 2 =", root2)
    elif discriminant == 0: # if discriminant ==0 there is one distinct root, if not then two complex roots
        root = -b / (2 * a)
        print("One real and repeated root:")
        print("Root =", root)
    else:
        print("The equation has complex (imaginary) roots.")
