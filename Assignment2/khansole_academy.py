"""
File: khansole_academy.py
-------------------------
Good practice adding two 2-digit integers
"""

import random
MIN_NUMBER = 10
MAX_NUMBER = 99
CORRECT_IN_A_ROW = 3

def khan_academy():
    corr_num = 0
    while corr_num < CORRECT_IN_A_ROW: # looping until which 3 corrections
        num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
        num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
        print("What is " + str(num1) + " + " + str(num2) + "?")
        user_answer = int(input("Your answer: "))
        right_answer = num1 + num2
        if user_answer == right_answer:
            corr_num += 1
            print("Correct! You've gotten " + str(corr_num) + " correct in a row.")
        else:
            corr_num = 0
            print("Incorrect. The expected answer is " + str(right_answer))
    print("Congratulations! You mastered addition.")


def main():
    khan_academy()


# This provided line is required at the end of a Python file
# to call the main() function.
if __name__ == '__main__':
    main()
