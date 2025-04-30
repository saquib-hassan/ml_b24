# Write a Python program to swap the values of two variables without using a temporary variable.
a = 5
b = 10

print("Before swapping: a =", a, "b =", b)
 
temp =a
a = b
b = temp


print("After swapping: a =", a, "b =", b)