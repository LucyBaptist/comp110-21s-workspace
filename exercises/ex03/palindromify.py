"""EX03 - palindromify function."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))
    return None


def palindromify(word: str, tf: bool) -> str:
    """Makes a palindrome."""
    num: int = len(word) - 1
    pal: str = ""
    if tf is True:
        while num >= 0:
            pal = pal + word[num]
            num = num - 1
    else:
        while num >= 1:
            pal = pal + word[num - 1]
            num = num - 1 
    return(word + pal)
            

if __name__ == "__main__":
    main()