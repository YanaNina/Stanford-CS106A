"""
File: hailstones.py
-------------------
program that reads in a number from the user and then displays
the Hailstone sequence for that number
"""

def hailstone():
    num = int(input("Enter a number: "))
    result = 0
    steps = 0
    while result != 1:
        if num % 2 == 1:
            result = num * 3 + 1
            print(str(num) + " is odd, so I make 3n + 1: " + str(result))
            num = result
        else:
            result = num // 2
            print(str(num) + " is even, so I take half: " + str(result))
            num = result
        steps += 1
    print("The process took " + str(steps) + " steps to reach 1")
def main():
    hailstone()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
