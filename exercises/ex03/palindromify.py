"""EX03 - palindromify function."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(palindromify("race", False))
    print(palindromify("han", True))
    print(palindromify("red", True))
    print(palindromify("live on time ", False))


def palindromify(word: str, tf: bool) -> str:
    num: int = len(word)
    pal: str = ""
    if tf == True:
        while num >= 0:
            pal += word[num]
            num -= 1
    else:
        while num >= 1:
            pal += word[num - 1]
            num -= 1 
    return(word + pal)
            

if __name__ == "__main__":
    main()