"""Advent of Code: Day 6"""

def instructions_to_list(instructions_file):
    with open(instructions_file) as file:
        inst_list = [line.rstrip('\n') for line in file]

    return inst_list


def lighting(instructions_list):
    """Constructs a dictionary representing a grid of lights, then follows instructions provided.

    The value of each pair of coords indicates whether the light at that coord is turned on.
    True = light on
    False = light off
    """

    lights = {}
    lights_on = 0

    for coord1 in range(0, 1000):
        for coord2 in range(0, 1000):
            lights[(coord1, coord2)] = False

    for each in instructions_list:
        each = each.split()

        if each[0] == "toggle":
            coords = instructions_to_coords([each[1], each[3]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    lights[(key1, key2)] = not lights[(key1, key2)]

        elif each[1] == "on":
            coords = instructions_to_coords([each[2], each[4]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    lights[(key1, key2)] = True

        elif each[1] == "off":
            coords = instructions_to_coords([each[2], each[4]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    lights[(key1, key2)] = False

    for value in lights.values():
        if value is True:
            lights_on += 1

    return lights_on


def lighting_2(instructions_list):
    """Constructs a dictionary representing a grid of lights, then follows instructions provided.

    The value of each pair of coords indicates the brightness of the light at that coord.
    """

    lights = {}
    brightness = 0

    for coord1 in range(0, 1000):
        for coord2 in range(0, 1000):
            lights[(coord1, coord2)] = 0

    for each in instructions_list:
        each = each.split()

        if each[0] == "toggle":
            coords = instructions_to_coords([each[1], each[3]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    lights[(key1, key2)] += 2

        elif each[1] == "on":
            coords = instructions_to_coords([each[2], each[4]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    lights[(key1, key2)] += 1

        elif each[1] == "off":
            coords = instructions_to_coords([each[2], each[4]])

            for key1 in range(coords[0], coords[2] + 1):
                for key2 in range(coords[1], coords[3] + 1):
                    if lights[(key1, key2)] > 0:
                        lights[(key1, key2)] -= 1

    for value in lights.values():
        brightness += value

    return brightness


def instructions_to_coords(coords_list):
    """Returns a tuple of integers representing the coords input."""

    c1, c2 = coords_list[0].split(',')
    c3, c4 = coords_list[1].split(',')
    c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4)

    return (c1, c2, c3, c4)

