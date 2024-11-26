def add(n1, n2):
    return n1 + n2

my_favourite_operation = add
print(my_favourite_operation(2 , 3))
#TODO: Wrte out the other 3 functions - subtarct, multiply and divide.
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2
#TODO: Add these 4 functions into a dictionary as the values. keys = "+", "-", "*", "/"
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
#TODO: Use the dictionary operations to perform the calculations. Multiply 4 * * using the dictionary
print(operations["*"](4,8))
print(operations["-"](8,4))
print(operations["+"](8,4))
print(operations["/"](8,4))
