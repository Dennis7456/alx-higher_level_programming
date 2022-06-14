#!/usr/bin/python3

import random

'''This program will assign a random signed
number to the variable number each time it
is executed. Complete the source code
in order to print the last digit of
the number stored in
the variable number.'''

number = random.randint(-10000, 10000)
last_digit = int(repr(number)[-1])
if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
else:
    print(f"Last digit of {number} is \
{last_digit} and is less than 6 and not 0")
