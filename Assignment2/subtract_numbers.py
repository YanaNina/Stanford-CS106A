"""
File: subtract_numbers.py
-------------------------
This program gets two real-values from the user and prints
the first number minus the second number.
"""

def sandcastles():
    print("This program subtracts one number from another.")
    result = float(input("Enter first number: ")) - float(input("Enter second number: "))
    # num2 = float(input("Enter second number:"))
    # result = num1 - num2
    print("The result is " + str(result))

def main():
    sandcastles()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
