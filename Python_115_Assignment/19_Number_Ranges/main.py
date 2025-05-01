# Write a Python program that takes an integer as input and prints whether the number falls within -
# the ranges: 0-50, 51-100, 101-150, or above 150.

try:
    num = int(input("Enter an integer: "))

    if 0 <= num <= 50:
        print("The number is in the range 0-50.")
    elif 51 <= num <= 100:
        print("The number is in the range 51-100.")
    elif 101 <= num <= 150:
        print("The number is in the range 101-150.")
    elif num > 150:
        print("The number is above 150.")
    else:
        print("The number is below 0.")

except ValueError:
    print("Please enter a valid integer.")