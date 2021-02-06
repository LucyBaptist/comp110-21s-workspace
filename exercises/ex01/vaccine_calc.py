"""A vaccination calculator."""

__author__ = "730386091"

# The datetime data type is imported from the datetime library.
# A datetime object models a specific date and time.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime-objects
from datetime import datetime

# The timedelta data type is imported from the timedelta library.
# A timedelta object models a "time span", such as 1 day or 1 hour and 3 minutes.
# Subtracting two datetime objects will result in the timedelta between them.
# Adding a datetime and a timedelta will result in the datetime offset by the timedelta.
#
# Official Documentation: https://docs.python.org/3/library/datetime.html#datetime.timedelta
from datetime import timedelta


# Begin your solution here...

today: datetime = datetime.today()

one_day: timedelta = timedelta(1)

tomorrow: datetime = today + one_day



pop = int(input("Population: "))
doses_admin = int(input("Doses administered: "))
doses_day = int(input("Doses per day: "))
target_percent = int(input("Target percent vaccinated: "))

math = ((target_percent / 100) * (pop * 2) - doses_admin) / doses_day

day = (round(math))

time_pass: timedelta = timedelta(day)

future: datetime = today + time_pass

print("We will reach " + str(target_percent) + "% vaccination in " + str(day) + " days, which falls on " + (future.strftime("%B %d, %Y")))
