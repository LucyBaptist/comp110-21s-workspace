"""Tar Heels exercise redux as a structured program."""

__author__ = "730386091"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    choice: int = int(input("Enter an int: "))
    print(tar_heel(choice))
    return None

def tar_heel(choice: int) -> str:
    if choice % 2 == 0 and choice % 7 == 0:
        return("TAR HEELS")
    if choice % 2 == 0 and choice % 7 != 0:
        return("TAR")
    if choice % 7 == 0 and choice % 2 != 0:
        return("HEELS")
    if choice % 7 != 0 and choice % 2 != 0:
        return("CAROLINA")

if __name__ == "__main__":
    main()