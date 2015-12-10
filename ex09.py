"""Advent of Code: Day 9"""

from itertools import permutations

def distances_to_list(file):
    with open(file) as file:
        return [line.rstrip('\n') for line in file]

def find_path_lens(distances_file):
    """Returns a tuple of the longest and shortest routes to all points."""
    
    distances = distances_to_list(distances_file)
    points = set()
    dist_dict = {}
    shortest_path = 1000000
    longest_path = 0

    for each in distances:
        each = each.split()
        points.update([each[0], each[2]])
        dist_dict[(each[0], each[2])] = each[4]

    routes = set(permutations(points))
    print routes

    for route in routes:
        num = 0
        dists = []
        for i in range(0, len(route) - 1):
            add = dist_dict.get((route[i], route[i + 1]))
            if add is None:
                add = dist_dict.get((route[i + 1], route[i]))
            num += int(add)
            dists.append(int(add))
        shortest_path = min([shortest_path, num])
        longest_path = max([longest_path, num])

    return (longest_path, shortest_path)

