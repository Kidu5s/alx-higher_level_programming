#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str = "Last digit of {} is {} and is"
if number > 0 and number % 10 > 5:
    print(str.format(number, number % 10), "greater than 5")
elif number % 10 == 0:
    print(str.format(number, number % 10), "0")
elif number < 0:
    print(str.format(number, -(-number % 10)), "less than 6 and not 0")
elif number > 0 or number < 6:
    print(str.format(number, number % 10), "less than 6 and not 0")
