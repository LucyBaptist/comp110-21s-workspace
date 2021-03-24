"""Utility functions for wrangling data."""

__author__ = "730386091"


from csv import DictReader



def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []
    file_handle = open(csv_file, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


def column_values(a: list[dict[str, str]], b: str) -> list[str]:
    """Finds column values."""
    columns = []
    for row in a:
        columns.append(row[b])
    return columns


def columnar(x: list[dict[str, str]]) -> dict[str, list[str]]:
    """Table to dictionary."""
    dictionary = {}
    for col in x:
        for item in col.keys():
            lst = column_values(x, item)
            dictionary[item] = lst
    return dictionary


def head(table: dict[str, list[str]], row_num: int) -> dict[str, list[str]]:
    """Table with rows of data."""
    dictionary = {}
    for column in table:
        list_col = []
        i: int = 0
        while i < row_num:
            
            i += 1
        dictionary[column] = list_col
    return dictionary


def select(dct: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Specific subset."""
    dictionary = {}
    for item in names:
        if item in dct:
            dictionary[item] = dct[item]
            return dictionary
        else: 
            return dictionary
    return dictionary


def count(l: list[str]) -> dict[str, int]:
    """Counts."""
    dictionary = {}
    for item in l:
        if item in dictionary:
            dictionary[item] += 1
        else: 
            dictionary[item] = 1
    return dictionary