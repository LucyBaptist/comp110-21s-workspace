"""EX03 - avoid_fifth function."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    # Put print statements here to test your function
    # ex. print(avoid_fifth("hello there"))


def avoid_fifth(words: str) -> str:
    """Removes e."""
    while "e" in words == True:
       words.strip("e")
    return words


if __name__ == "__main__":
    main()