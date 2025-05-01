#Write a Python program that takes a number as input and prints whether it is positive, negative, or zero.

num = int(input("Enter a number: "))
if num == 0:
    print("The number is zero")
elif num < 0:
    print("The number is negative")
else:
    print("The number is positive")