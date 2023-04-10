__author__ = "730408563"

from csv import DictReader

def read_csv_rows(filename: str) -> list [dict[str,str]]:
    """Read csv file and return as a list of dicts with header keys."""
    result: list[dict[str,str]] = []
    file_handle = open(filename, "r", encoding = "utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        result.append(row)
    file_handle.close ()
    return result 


def column_values(table: list[dict[str, str]], column_num: str) -> list[str]:
    """Makes a list of all values in a column."""
    result: list[str] = []
    for row in table:
        value: str = row[column_num]
        result.append(value)
    return result    


def columnar(row: list[dict[str, str]]) -> dict[str, list [str]]:
    """Makes a table of rows into a table of columns."""
    result: dict [str, list[str]] = {}
    row_1: dict [str, str] = row[0]
    for column in row_1:
        result[column] = column_values(row,column)
    return result

def head(d: dict[str, list[str]], xs: int) -> dict[str, list[str]]:
    """Makes a column-based table with the first value from each row."""
    result: dict[str, list[str]] = {}
    if xs >= len(d):
        return d
    for key in d:
        value: list[str] = []
        i: int = 0 
        while i < xs:
            value.append (d[key][i])
            i += 1
        result[key] = value
    return result 


def select (norm: dict[str, list[str]], info: list[str]) -> dict[str, list[str]]:
    """This produces a column based table with specific values from the original set."""
    i: int = 0
    result: dict[str, list[str]] = {}
    while i < len(info):
        result[info[i]] = norm[info [i]]
        i += 1
    return result


def concat (num_1: dict[str, list[str]], num_2: dict [str, list[str]]) -> dict[str, list[str]]:
    """This function combines two column based tables."""
    result: dict[str, list[str]] = {}
    for key in num_1:
        result[key] = num_1[key]
    for key in num_2:
        if key in result:
            i: int = 0
            while i < len(num_2[key]):
                result[key].append(num_2[key][i])
                i += 1 
        else:
            result[key] = num_2[key]
    return result


def count (a: list[str]) -> dict[str, int]:
    """Counts the number of times a term is repeated within a list."""
    result: dict [str, int] = {}
    for i in a:
        if i in result:
            result [i] += 1 
        else:
            result [i] = 1
    return result