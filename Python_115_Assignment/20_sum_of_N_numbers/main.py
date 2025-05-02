# Write a Python program using a for loop to calculate the sum of the first N natural numbers, 
# where N is taken as input from the user.

N = int(input("Enter a natural number between 1 to 100: "))

total = 0

for i in range(1, N+1):
    total += i

print(f"Sum of {N} numbers is {total}")