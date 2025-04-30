# Write a Python function to reverse a given string and return the reversed string.

def rev_txt(x):
    return x[::-1]

text = input("Enter a text: ")
print(rev_txt(text))