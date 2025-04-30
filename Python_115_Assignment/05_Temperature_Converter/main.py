# Write a Python program that converts a temperature in Celsius to Fahrenheit. 
# Take the Celsius temperature as input from the user.

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"{celsius}°C is equal to {fahrenheit}°F")