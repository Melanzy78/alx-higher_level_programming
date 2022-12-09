#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if number < 0:
<<<<<<< HEAD
digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
print("greater than 5")
elif digit == 0:
print("0")
else:
print("less than 6 and not 0")
=======
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and is ", end="")
if digit > 5:
    print("greater than 5")
elif digit == 0:
    print("0")
else:
    print("less than 6 and not 0")
>>>>>>> 82b7305138ae38f014f692c5dea7bb74ceb3669d
