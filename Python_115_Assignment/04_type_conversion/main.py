# Given a list of integers, write a Python program to convert each element of the list to a string.


list_of_int = [1, 2, 3, 4, 5, 6, 7]
list_of_str = []
for i in list_of_int:
    list_of_str.append(str(i))

print(f"List of strings: {list_of_str}")