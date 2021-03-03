"""EX03 - avoid_fifth function."""

__author__: str = "730386091"


def main() -> None:
    """Entrypoint of the program."""
    print(avoid_fifth("three"))
    print(avoid_fifth("hello"))
    print(avoid_fifth("The sentence we have here possesses E's galore!"))


def avoid_fifth(words: str) -> str:
    """Removes e."""
    if "e" in words:
        new_words:str = words.rstrip("e")
        return new_words
    return words

       

if __name__ == "__main__":
    main()