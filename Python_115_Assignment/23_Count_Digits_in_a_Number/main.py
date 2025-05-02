# Write a Python program using a while loop to count the number of digits in a given integer N.

N = int(input("Enter a positive integer: "))

count = 1 if N == 0 else 0

while N > 0:
    N //= 10 
    # if the given input is 456, N becomes 45
    count += 1

print("Number of digits:", count)