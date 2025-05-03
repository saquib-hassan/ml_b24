# Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, 
# and minimum values in the list.

numbers = [21, 1, 9, 12, 5, 6]

if not numbers:
    print("List is empty!")
else:
    total = 0
    max = min = numbers[0] 
    
    for num in numbers:
        total += num
        if num > max:
            max = num
        if num < min:
            min = num
    
    avg = total / len(numbers)
    
    print(f"Sum: {total}")
    print(f"Average: {avg}")
    print(f"Maximum: {max}")
    print(f"Minimum: {min}")

