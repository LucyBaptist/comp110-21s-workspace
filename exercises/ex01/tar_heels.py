"""An exercise in remainders and boolean logic."""

__author__ = "730386091"


# Begin your solution here...
user_num = int(input("Please enter an int: "))

if user_num % 2 == 0 and user_num % 7 == 0:
    print("TAR HEELS")

if user_num % 2 == 0 and user_num % 7 != 0:
    print("TAR")

if user_num % 7 == 0 and user_num % 2 != 0:
    print("HEELS")

if user_num % 7 != 0 and user_num % 2 != 0:
    print("CAROLINA")