# Write a Python function that takes a variable as input and returns the data type of the variable as a string 
# (e.g., “int”, “float”, “str”, “list”, etc.).

def var_type(variable):
    return type(variable)

list_of_variables = [23,"Saquib",True,23.68,[1,2,3]]

for i in list_of_variables:
    print(f"Variable: {i} Type: {var_type(i)}")