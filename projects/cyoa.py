__author__ = "730386091"

ANSWER_ONE: int = 1
ANSWER_TWO: int = 30
ANSWER_THREE: int = 100

def main() -> None:
    """Entry point."""
    print(greet())
    print(question_1())
    print(question_2())
    print(question_3())


def greet() -> None:
    """A way to introduce the player to the program."""
    print("Hello! This quiz will assign a sci-fi book series based on a series of questions that you wil answer.")
    print("Enter a name, then begin the quiz.")
    player: str = str(input("Please enter a name: "))
    return player

def question_1(a_1: str) -> str:
    """Question 1."""
    print("Which of these emojis reflects a setting that you are interested?")
    print("a. \U0001F307 \n b. \U0001F304 \n c. \U0001F3DE ")
    a_1 = str(input("Please enter the letter of your answer here: "))
    return a_1

def question_2() -> str:
    """Question 2."""
    a_2 = str(input("Please enter the letter of your answer here: "))
    return a_2

def question_3() -> str:
    """Question 3."""
    a_3 = str(input("Please enter the letter of your answer here: "))
    return a_3

def point_keeping(ans_1: str, ans_2: str, ans_3: str) -> int:
    """A way of keeping track of points to determine results."""
    ans_1 = a_1
    ans_2 = a_2
    ans_3 = a_3
    if ans_1 = a
        then ans_1 = ANSWER_ONE
    if ans_1 = b
        then ans_1 = ANSWER_TWO
    if ans_1 = c
        then ans_1 = ANSWER_THREE




if __name__ == "__main__":
  main()