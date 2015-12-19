"""Advent of Code: Day 18"""

from itertools import product
from math import sqrt

def file_to_light_rows(light_file):
    with open(light_file) as file:
        light_rows = [line.rstrip('\n') for line in file]
    return light_rows


def make_light_dict(light_rows):
    """Generates a dictionary of light coords from a list of rows in lights file.
    """

    light_dict = {}
    for x, row in enumerate(light_rows):
        for y, char in enumerate(row):
            # Char '#' indicates the light is on
            if char == '#':
                light_dict[(x, y)] = True
            # Char '.' indicates the light is off
            elif char == '.':
                light_dict[(x, y)] = False

    return light_dict


def corners_stuck(light_dict, max_coord):
    """Sets the four corner lights to on (True).
    """

    # Corners coords will have both values be either the max or the min coord
    corners = set(product((0, max_coord), repeat=2))
    for corner in corners:
        light_dict[corner] = True

    return light_dict


def adjacent_coords(coord, max_coord):
    """Finds the coords adjacent to a given light coord.
    """

    coords = []
    for x in range(coord[0] - 1, coord[0] + 2):
        for y in range(coord[1] - 1, coord[1] + 2):
            if x in range(0, 100) and y in range(0, 100) and (x, y) != coord:
                coords.append((x, y))
    return coords


def iterate_lights(light_dict, max_coord):
    """Generates a new dictionary of lights after one iteration.
    """

    new_dict = {}
    for light in light_dict:
        adjacent = adjacent_coords(light, max_coord)
        num_on = 0
        for ea in adjacent:
            if light_dict[ea] is True:
                num_on += 1
        if light_dict[light] is True and num_on not in (2, 3):
            new_dict[light] = False
        elif light_dict[light] is False and num_on == 3:
            new_dict[light] = True
        else:
            new_dict[light] = light_dict[light]
    return new_dict


def find_num_lights_on(light_file, iterations):
    """Finds the number of lights on (True) after a given number of iterations.
    """

    light_rows = file_to_light_rows(light_file)
    light_dict = make_light_dict(light_rows)
    # The sq rt of the number of coords, minus 1, is the max coord value
    max_coord = int(sqrt(len(light_dict))) - 1
    lights_on = 0

    count = 0
    while count < iterations:
        light_dict = corners_stuck(iterate_lights(light_dict, max_coord), max_coord)
        count += 1

    for value in light_dict.values():
        if value is True:
            lights_on += 1

    return lights_on


print find_num_lights_on('ex18.txt', 100)



