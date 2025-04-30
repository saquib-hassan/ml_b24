# Write a Python function to reverse a given string using slicing.

def reverse_string(text):
    return text[::-1]

test_string = ["hello","Saquib", "Harvard","Cornell", "765"]
for i in test_string:
    print(f"String {i} after reversed: {reverse_string(i)}")