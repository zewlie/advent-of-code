"""Advent of Code: Day 3"""

def num_received_gifts(instructions):
    """Returns the number of houses (coords) visited from instructions.

    Instructions work as follows:
     - '^' indicates one move North
     - 'v' indicates one move South
     - '<' indicates one move West
     - '>' indicates one move East

    Houses/coords can be visited many times, but only the first visit is counted.
    """

    current_loc = (0, 0)
    visited = set()
    visited.add(current_loc)

    for char in instructions:
        current_loc = move(current_loc, char)
        visited.add(current_loc)

    return len(visited)


def num_received_gifts_w_robosanta(instructions):
    """Returns the number of houses (coords) visited from instructions.
    Santa and RoboSanta alternate taking individual instructions.

    Instructions work as follows:
     - '^' indicates one move North
     - 'v' indicates one move South
     - '<' indicates one move West
     - '>' indicates one move East

    Houses/coords can be visited many times, but only the first visit is counted.
    """

    santa_loc = (0, 0)
    robosanta_loc = (0, 0)
    visited = set()
    visited.add(santa_loc)

    for i, char in enumerate(instructions):
        if i == 0 or i % 2 == 0:
            current_loc = santa_loc
        else:
            current_loc = robosanta_loc

        current_loc = move(current_loc, char)

        if i == 0 or i % 2 == 0:
            santa_loc = current_loc
        else:
            robosanta_loc = current_loc

        visited.add(current_loc)

    return len(visited)


def move(current_loc, char):
    """Makes one move N, S, E, or W, and returns the new current location."""

    if char == '>':
        current_loc = (current_loc[0], current_loc[1] + 1)
    elif char == '<':
        current_loc = (current_loc[0], current_loc[1] - 1)
    elif char == '^':
        current_loc = (current_loc[0] + 1, current_loc[1])
    elif char == 'v':
        current_loc = (current_loc[0] - 1, current_loc[1])

    return current_loc

