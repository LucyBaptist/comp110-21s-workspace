__author__ = "730386091"

from random import randint

ANSWER_ONE: int = 1
ANSWER_TWO: int = 30
ANSWER_THREE: int = 100

while input("Would you like to continue? yes/no: ") == "yes":
    count: int = 0
    def main() -> None:
        """Entry point."""
        print(greet())
        result = (input("Type CONTINUE or RANDOM: "))
        print(question_1())
        a_1: str = str(input("Please enter the letter of your answer here: "))
        print(question_2())
        a_2: str = str(input("Please enter the letter of your answer here: "))
        print(question_3())
        a_3: str = str(input("Please enter the letter of your answer here: "))
        print(point_keeping(a_1, a_2, a_3))
        
        count += 1
        print(f"You have taken this quiz {count} times.")

print(f"{player}, thank you for taking my quiz!")


def greet() -> None:
    """A way to introduce the player to the program."""
    print("Hello! This quiz will assign a sci-fi book series based on a series of questions that you wil answer.")
    print("Enter a name, then begin the quiz.")
    player: str = str(input("Please enter a name: "))
    print(f"{player}, would you like to take the quiz or generate a random answer?")
    return None


def question_1() -> None:
    """Question 1."""
    print("Which of these emojis reflects a setting that you are interested?")
    print("a. \U0001F307 \n b. \U0001F304 \n c. \U0001F3DE ")
    return None


def question_2() -> None:
    """Question 2."""
    print("Do you like aliens in fiction?")
    print("a. no \n b. yes, but only if they're basically humans \n c. yes, the more alien the better")
    return None


def question_3() -> None:
    """Question 3."""
    print("How would you like the book serie sto make you feel?")
    print("a. \U0001F914 \n b. \U0001F92F \n c. \U0001F62E")
    a_3 = str(input("Please enter the letter of your answer here: "))
    return None


def point_keeping(ans_1: str, ans_2: str, ans_3: str) -> int:
    """A way of keeping track of points to determine results."""
    if ans_1 == "a":
        return ANSWER_ONE
    if ans_1 == "b":
        return ANSWER_TWO
    if ans_1 == "c":
        return ANSWER_THREE
    if ans_2 == "a":
        return ANSWER_THREE
    if ans_2 == "b":
        return ANSWER_TWO
    if ans_2 == "c":
        return ANSWER_THREE
    if ans_3 == "a":
        return ANSWER_TWO
    if ans_3 == "b":
        return ANSWER_ONE
    if ans_3 == "c":
        return ANSWER_THREE



def answer(score: int) -> str:
    """Gives the result of the quiz."""





if __name__ == "__main__":
  main()