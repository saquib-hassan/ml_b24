# Write a Python program that takes the time in hours (24-hour format) as input and prints “Good Morning”, “Good Afternoon”, 
# “Good Evening”, or “Good Night” based on the time.

hour= int(input("Enter the hour (0–23): ")) # in the 24-hour clock, hours run from 0 up to 23

try:
    if not (0 <= hour <= 23):
        raise ValueError()
    

    if 0 <= hour < 12:
        greeting = "Good Morning"
    elif 12 <= hour < 17:
        greeting = "Good Afternoon"
    elif 17 <= hour < 21:
        greeting = "Good Evening"
    else:
        greeting = "Good Night"

    print(greeting)

except ValueError:

    print("Please enter a valid integer hour between 0 and 23.")

