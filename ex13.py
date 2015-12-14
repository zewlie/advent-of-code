"""Advent of Code: Day 13"""

from itertools import permutations


def make_happiness_dict(file):
    """Generates a dictionary of dictionaries representing every possible pair
    of party-goers who might be seated together, and their happiness gain/loss.
    """

    h_dict = {}
    with open(file) as file:
        for line in file:
            line = line.split()
            person1, person2, neg, value = line[0], line[10][:-1], line[2] == 'lose', int(line[3])
            if neg:
                value = -(value)
            if h_dict.get(line[0]) is None:
                h_dict[person1] = {}
            h_dict[person1][person2] = value
    return h_dict


def find_best_order(h_dict):
    """Finds the highest possible happiness gain (or lowest loss) from any seating arrangement.
    """

    best = -1000
    orders = set(permutations(h_dict.keys()))
    for order in orders:
        value = 0
        for i in range(0, len(order)):
            if i == len(order) - 1:
                value += h_dict[order[i]][order[0]]
                value += h_dict[order[0]][order[i]]
            else:
                value += h_dict[order[i]][order[i + 1]]
                value += h_dict[order[i + 1]][order[i]]
        if value > best:
            best = value
            print value
            print order

    return best


def make_happiness_dict_2(file):
    """Generates a dictionary of dictionaries representing every possible pair
    of party-goers who might be seated together, and their happiness gain/loss.

    Includes me; I do not gain or lose happiness based on who I am seated with.
    Likewise, the people seated next to me do not gain or lose happiness.
    """

    h_dict = {"me": {}}
    with open(file) as file:
        for line in file:
            line = line.split()
            person1, person2, neg, value = line[0], line[10][:-1], line[2] == 'lose', int(line[3])
            if neg:
                value = -(value)
            if h_dict.get(line[0]) is None:
                h_dict[person1] = {}
            h_dict[person1][person2] = value

    for person in h_dict.keys():
        if person != "me":
            h_dict["me"][person] = 0
            h_dict[person]["me"] = 0

    return h_dict
