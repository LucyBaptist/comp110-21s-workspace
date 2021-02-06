"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730386091"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
fortune = randint(1, 100)
print("Your fortune cookie says...")
if fortune < 60:
    if fortune < 30:
        print("You will find a pleasant surprise next week.")
    else:
        print("Someone will have good news for you soon.")
if fortune < 85:
    if fortune < 70:
        print("Be on the watch for a new opportunity.")
    else:
        print("Expect to find a new friend in an unexpected place.")
else:
    print("Try your best, success is within your reach.")
print("Now, go spread positive vibes!")