# Write a Python program that takes a single character as input and determines whether it is a vowel or a consonant.
char = input("Enter a single character: ").lower()
vowels = ["a","e","i","o","u"]

if len(char) != 1 or not char.isalpha():
    print("Please enter a single alphabet character.")
else:

    if char in vowels:
        print("vowel")
    else:
        print("Consonant")

