# Write a Python program that takes three numbers as input and prints the largest among them.

for i in range(3):
    num = int(input("Enter a number: "))
    max_num = 0
    if num > max_num:
        max_num = num
print(f"{max_num} is the largest among them")