# Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.


# for _ in range(5):
#     print("Hello")

N = int(input("Enter the limit for the Fibonacci sequence: "))

a, b = 0, 1
for _ in range(N):
    if a > N:
        break
    print(a, end=" ")
    a, b = b, a + b
    # a becomes b and b becomes the sum of a and b

