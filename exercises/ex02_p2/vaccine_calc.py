"""Vaccine calculator exercise as a structured program."""

from datetime import datetime, timedelta

__author__ = "730386091"


def main() -> None:
    """The entrypoint of the program, when run as a module."""
    population: int = int(input("Population: "))
    doses: int = int(input("Doses administered: "))
    doses_per_day: int = int(input("Doses per day: "))
    target: int = int(input("Target percent vaccinated: "))
    days = days_to_target(population, doses, doses_per_day, target)
    some_future = future_date(days)
    print("We will reach " + str(target) + "% vaccination in " + str(days) + " days, which falls on " + some_future)


def days_to_target(population: int, doses: int, doses_per_day: int, target: int) -> int:
    """Gives the number of days until target."""
    math = ((target / 100) * (population * 2) - doses) / doses_per_day
    return(round(math))


def future_date(num_days: int) -> str:
    """Gives the date given number of days."""
    today: datetime = datetime.today()
    time_pass: timedelta = timedelta(num_days)
    future: datetime = today + time_pass
    future_f = future.strftime("%B %d, %Y")
    return(future_f)


if __name__ == "__main__":
    main()
