"""Advent of Code: Day 1"""

def find_floor(inst):
    """Prints a tuple: the floor Santa ends up on, and the index of the instruction
    that first results in him entering the basement (floor -1).

    Instructions (arg) work as follows:
    - Open parens -> go up one floor.
    - Closed parens -> go down one floor.
    """

    floor = 0
    enter_bm = None

    for i, char in enumerate(inst):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if enter_bm == None and floor < 0:
                enter_bm = i + 1

    return (floor, enter_bm)
