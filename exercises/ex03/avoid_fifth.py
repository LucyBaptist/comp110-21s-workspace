"""EX03 - avoid_fifth function."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("three"))
    print(avoid_fifth("print"))
    print(avoid_fifth("Hello World!"))


def avoid_fifth(sentence: str) -> str:
    """Removes e."""
    words: str = sentence
    indx: int = 0
    result: str = ""
    while indx <= len(words):
        if words[indx] == "e" or words[indx] == "E":
            indx += 1
        else:
            result += "words"[indx]
            indx += 1
    return result

       

if __name__ == "__main__":
    main()