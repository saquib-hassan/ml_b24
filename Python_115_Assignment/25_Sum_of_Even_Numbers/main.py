# Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, 
# where N is taken as input from the user.

N = int(input("enter a number: "))

sum_of_even = 0
number_starts_from = 2

while number_starts_from <= N:
    if number_starts_from % 2 ==0:
        sum_of_even += number_starts_from
    number_starts_from += 1

print(f"Sum of even numbers between 1 and {N} is: {sum_of_even}")