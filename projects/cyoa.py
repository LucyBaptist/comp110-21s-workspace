__author__ = "730386091"

from random import randint

ANSWER_ONE: int = 1
ANSWER_TWO: int = 30
ANSWER_THREE: int = 100
EYE_ROLL: str = "\U0001F644"


def main() -> None:
    """Entry point."""
    count: int = 0
    while input("Would you like to continue the quiz? yes/no: ") == "yes":
        print(greet())
        result = (input("Type CONTINUE or RANDOM: "))
        if result == "CONTINUE":
            print("Which of these emojis reflects a setting that you are interested?")
            print("a. \U0001F307 \n b. \U0001F304 \n c. \U0001F3DE ")
            a_1: str = str(input("Please enter the letter of your answer here: "))
            print("Do you like aliens in fiction?")
            print("a. no \n b. yes, but only if they're basically humans \n c. yes, the more alien the better")
            a_2: str = str(input("Please enter the letter of your answer here: "))
            print("How would you like the book serie sto make you feel?")
            print("a. \U0001F914 \n b. \U0001F92F \n c. \U0001F62E")
            a_3: str = str(input("Please enter the letter of your answer here: "))
            first: int = point_keeping_one(a_1)
            second: int = point_keeping_two(a_2)
            third: int = point_keeping_three(a_3)
            points = points_total(first, second, third)
            print(answer(points))
        else:
            rand_result = (input(f"{player}, would you prefer to TYPE an integer or GENERATE?: "))
            if rand_result == "TYPE":
                number = int(input("Pease type an integer between 1 and 300 here: ")) # add function or something
                print(answer(number))
            if rand_result == "GENERATE":
                number = int(randint(1, 300))
                print(answer(number))
        count += 1
        print(f"You have taken this quiz {count} times")
        print(f"{player}, thank you for taking my quiz!")
        

def greet() -> None:
    """A way to introduce the player to the program."""
    print("Hello! This quiz will assign a sci-fi book series based on a series of questions that you wil answer.")
    print("Enter a name, then begin the quiz.")
    global player
    player: str = str(input("Please enter a name: "))
    print(f"{player}, would you like to take the quiz or generate a random answer?")
    return None


def point_keeping_one(ans_1: str) -> int:
    """Gives the score for one."""
    if ans_1 == "a":
        return ANSWER_ONE
    if ans_1 == "b":
        return ANSWER_TWO
    return ANSWER_THREE


def point_keeping_two(ans_2: str) -> int:
    """Gives the score for one."""
    if ans_2 == "a":
        return ANSWER_THREE
    if ans_2 == "b":
        return ANSWER_TWO
    return ANSWER_THREE


def point_keeping_three(ans_3: str) -> int:
    """Gives the score for three."""
    if ans_3 == "a":
        return ANSWER_TWO
    if ans_3 == "b":
        return ANSWER_ONE
    return ANSWER_THREE


def points_total(f: int, s: int, t: int) -> int:
    """Gives the total points."""
    total = int(f + s + t)
    return total


def answer(score: int) -> str:
    """Gives the result of the quiz."""
    if score < 33 and score > 0 or score == 102:
        return("You should read Remembrance of Earth's Past by Cixin Liu")
    if score > 32 and score < 100 or score == 160:
        return("You should read the Hainish Cycle by Ursula K. Le Guin")
    if score > 99 and score < 301:
        return("You should read the Broken Earth Trilogy by N. K. Jemisin")
    return(f"{EYE_ROLL}, I said between 1 and 300, read Wayfarers by Becky Chambers")


if __name__ == "__main__":
    main()