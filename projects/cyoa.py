__author__ = "730386091"

from typing import AnyStr


ANSWER_ONE: int = 1
ANSWER_TWO: int = 30
ANSWER_THREE: int = 100

def main() -> None:
    """Entry point."""
    print(greet())
    print(question_1())
    print(question_2())
    print(question_3())
    print(point_keeping(a_1, a_2, a_3))


def greet() -> None:
    """A way to introduce the player to the program."""
    print("Hello! This quiz will assign a sci-fi book series based on a series of questions that you wil answer.")
    print("Enter a name, then begin the quiz.")
    player: str = str(input("Please enter a name: "))
    print(player + "Would you like to take the quiz or generate a random answer?")
    result = (input("Type CONTINUE or RANDOM: "))
    return result


def question_1() -> str:
    """Question 1."""
    print("Which of these emojis reflects a setting that you are interested?")
    print("a. \U0001F307 \n b. \U0001F304 \n c. \U0001F3DE ")
    a_1 = str(input("Please enter the letter of your answer here: "))
    return a_1


def question_2() -> str:
    """Question 2."""
    print("Do you like aliens in fiction?")
    print("a. no \n b. yes, but only if they're basically humans \n c. yes, the more alien the better")
    a_2 = str(input("Please enter the letter of your answer here: "))
    return a_2


def question_3() -> str:
    """Question 3."""
    print("How would you like the book serie sto make you feel?")
    print("a. \U0001F914 \n b. \U0001F92F \n c. \U0001F62E")
    a_3 = str(input("Please enter the letter of your answer here: "))
    return a_3


def point_keeping(ans_1: str, ans_2: str, ans_3: str) -> int:
    """A way of keeping track of points to determine results."""
    if ans_1 = "a":
        then: ans_1 = ANSWER_ONE
    if ans_1 = "b":
        then: ans_1 = ANSWER_TWO
    if ans_1 = "c":
        then: ans_1 = ANSWER_THREE




if __name__ == "__main__":
  main()