"""Utility functions for wrangling data."""

__author__ = "730386091"


from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open("nc_durham_2015_march_21_to_27.csv", "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        print(row)

    file_handle.close()

    # TODO 0.1) Complete the implementation of this function here.
    return rows


# TODO: Define the other functions here.

def column_values(a: list[dict[str, str]], b: str) -> list[str]:
    columns: list[str] = []
    for row in a:
        columns.append(row)
    return columns


def columnar(x: list[dict[str, str]]) -> dict[str, list[str]]:
    dictionary = {}
    for col in x:
        return col
        