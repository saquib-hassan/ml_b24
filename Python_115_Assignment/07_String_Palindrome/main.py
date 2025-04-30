# Write a Python function to check if a given string is a palindrome or not.

def is_palindrom(text):
    return text == text[::-1] #reversing

test_string = ["Hello", "racecar", "abba","Rob","12321"]
for i in test_string:
    print(f"String {i} is palindrom: {is_palindrom(i)}")