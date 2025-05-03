# Write a Python program using a while loop to check if a given number N is prime or not.

n = int(input("Enter a number: "))

if n < 2:
    print("Not prime")
else:
    d = 2
    while d * d <= n:
        if n % d== 0:
            print("Not prime")
            break
        d = d + 1
    else:
        print("Prime")