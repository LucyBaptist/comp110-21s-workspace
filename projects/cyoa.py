__author__ = "730386091"

def main() -> None:
    """Entry point."""
    print(greet())
    print(question_1())

def greet() -> None:
    """A way to introduce the player to the program."""
    print("Hello! This quiz will assign a sci-fi book series based on a series of questions that you wil answer. Enter a name, then begin the quiz.")
    player: str = str(input("Please enter a name: "))
    return player

def question_1() -> str:
    """Question 1."""
    a_1: str = str(input("Please enter the letter of your answer here: "))
    return a_1






if __name__ == "__main__":
  main()