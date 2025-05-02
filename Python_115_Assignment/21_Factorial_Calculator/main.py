# Write a Python program using a while loop to calculate the factorial of a given number N.

N = int(input("Enter a number: "))

i = 1
fact = 1

while i<=N:
    fact = fact * i
    #5 = 1*2*3*4*5 = 120
    i = i+1

print(f"Factorial of {N} is {fact}")
