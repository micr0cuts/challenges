#pylint: disable=missing-module-docstring,invalid-name
from typing import List

from pathlib import Path

def inputgetter_list(fname: str) -> List[str]:
    ''' Reads in an input file
    and returns a list of strings
    where one line is one list.
    '''
    lines = []
    with Path(fname).open(encoding='utf8') as f:
        for line in f:
            lines.append(line.strip())
    return lines

def inputgetter_int_matrix(fname: str) -> List[List[int]]:
    '''Reads in an input file
    and returns a list of lists.
    Each character is mapped to int().
    Assumes that each character is a
    digit in range(0,10).
    '''
    matrix = []
    with open(fname, encoding='utf8') as f:
        for line in f:
            matrix.append([int(char) for char in line.strip()])
    return matrix

def print_matrix(m):
    '''
    Helper function for debugging.
    Prints one row per line
    and prints an empty line at the end
    '''
    for row in m:
        print(row)
    print()

def check_coordinates(x, y, m):
    '''
    Function to check if coordinates in a matrix are valid.
    The goal is to prevent coordinates going out of range.
    Written for day 11 but can be helpful on other days too.
    '''
    if x >= 0:
        if x < len(m):
            if y >= 0:
                if y < len(m[0]):
                    return True
    return False
