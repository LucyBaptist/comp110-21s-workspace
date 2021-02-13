"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730386091"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    # TODO 2: Call days_to_target and store result in a variable.
    days = days_to_target(population, doses, doses_per_day, target)
    # TODO 4: Call future_date and store result in a variable.
    some_future = future_date(days)
    # TODO 5: Print the expected output using the variables above.
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + some_future)

# TODO 1: Define days_to_target function
def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    math = ((target / 100) * (population * 2) - doses) / doses_per_day
    return(round(math))

# TODO 3: Define future_date function
def future_date(num_days: int) -> str:
    today: datetime = datetime.today()
    time_pass: timedelta = timedelta(num_days)
    future: datetime = today + time_pass
    future_f = future.strftime("%B %d, %Y")
    return(future_f)

if __name__ == "__main__":
    main()
