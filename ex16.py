"""Advent of Code: Day 16"""

def file_to_sue_dict(file):
    """Generates a dictionary of Aunt Sues and their item counts.
    """

    sues = {}
    with open(file) as file:
        for line in file:
            line = line.rstrip('\n').replace(':', ',', 1)
            line = line.split(',')
            sues[line[0]] = {}
            for item in line[1:]:
                item, qty = item.split(': ')
                sues[line[0]][item.lstrip()] = int(qty)
    return sues


def read_ticker_tape(file):
    """Generates a dictionary of requirements from the MFCSAM output.
    """

    reqs = {}
    with open(file) as file:
        for line in file:
            line = line.rstrip('\n')
            item, qty = line.split(':')
            reqs[item] = int(qty)
    return reqs


def find_sue_num(sue_file, tape_file):
    """Finds the Aunt Sue who meets the requirements specified by the MFCSAM output.
    """

    sues = file_to_sue_dict(sue_file)
    reqs = read_ticker_tape(tape_file)
    keys = reqs.keys()

    count = 0
    while len(sues) > 1:
        new_sues = {}
        for sue in sues:
            if keys[count] not in sues[sue] or reqs[keys[count]] == sues[sue].get(keys[count]):
                new_sues[sue] = sues[sue]
        sues = new_sues
        count += 1

    return sues


print find_sue_num('ex16.txt', 'ex16b.txt')

