"""
running exceptions example

how to handle working with exceptions
"""

try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))

    c = a / b
    print(c)
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")

print("continuing program")