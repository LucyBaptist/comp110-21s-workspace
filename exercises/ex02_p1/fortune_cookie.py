"""Fortune cookie exercise redux as a structured program."""

from random import randint

__author__ = "730386091"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    print("Your fortune cookie says...")
    print(fortune_cookie())
    print("Now, go spread positive vibes!")
    return None


def fortune_cookie(fortune=randint(0, 100)) -> str:
    if fortune < 60:
        if fortune < 30:
            return("You will find a pleasant surprise next week.")
        return("Someone will have good news for you soon.")
    if fortune < 85:
        if fortune < 70:
            return("Be on the watch for a new opportunity.")
        return("Expect to find a new friend in an unexpected place.")
    return("Try your best, success is within your reach.")

    
# Python Idiom for "starting" the program when run as a module.
# The special dunder variable __name__ will be "__main__" when run as module. 
if __name__ == "__main__":
    main()