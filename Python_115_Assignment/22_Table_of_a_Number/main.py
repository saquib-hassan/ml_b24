# Write a Python program using a for loop to print the multiplication table of a given number N.

num = int(input("Enter a number: "))
#i = 1
total = 0
for i in range(0,10):
    i = i+1
    total = num * i
    print(f"{num} * {i} = {total}")