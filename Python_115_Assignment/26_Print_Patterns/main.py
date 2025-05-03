# Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, 
# an inverted right-angled triangle, and so on.

# In this program - I'm going to demonstrate three diffrent patterns

# Right angled Triangle
R = int(input("Enter the number of rows for the right-angled triangle: "))
for i in range(1, R+1):
    for j in range(i):
        print("*", end="")
    print()

#------------------------------------------------------------------------------------#

# Inverted right angled Triangle
IR = int(input("Enter the number of rows for the inverted right-angled triangle: "))
for i in range(IR, 0, -1):
    for j in range(i):
        print("*", end="")
    print()


#--------------------------------------------------------------------------------------#

# Diamond pattern
D = int(input("Enter the number of rows for the diamond: "))

for i in range(1, D + 1):
    for j in range(D-i):
        print(" ", end="")
    for j in range(2 * i- 1):
        print("*", end="")
    print()


for i in range(D-1, 0, -1):
    for j in range(D - i):
        print(" ", end="")
    for j in range(2 * i- 1):
        print("*", end="")
    print()

