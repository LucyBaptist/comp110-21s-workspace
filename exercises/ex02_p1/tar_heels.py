"""Tar Heels exercise redux as a structured program."""

__author__ = "730386091"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heels(choice))
    return None


def tar_heels(choice: int) -> str:
    """Gives a word given integer input."""
    if choice % 2 == 0 and choice % 7 == 0:
        return("TAR HEELS")
    if choice % 2 == 0 and choice % 7 != 0:
        return("TAR")
    if choice % 7 == 0 and choice % 2 != 0:
        return("HEELS")
    if choice % 7 != 0 and choice % 2 != 0:
        return("CAROLINA")
    return("CAROLINA")


if __name__ == "__main__":
    main()