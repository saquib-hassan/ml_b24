# Write a Python program using a while loop to reverse a given string.

original_str = input("Enter a string: ")

reversed_str = ""
length = len(original_str)
index = length - 1 

while index >= 0:
    reversed_str += original_str[index]
    index = index - 1

print(f"Reversed string is: {reversed_str}")
