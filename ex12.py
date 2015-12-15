"""Advent of Code: Day 12"""

def read_file(file):
    with open(file) as file:
        json = file.read().replace('\n', '')
    return json

def sum_nums(json):
    """Sum all numbers in string; ignore other content."""
    num_list = []
    num = ''
    in_obj = 0
    red = False
    pending = []

    for i, char in enumerate(json):
        if char == '{':
            in_obj += 1
        elif char == '}':
            in_obj -= 1

        if in_obj > 0 and i < len(json) - 2 and json[i:i+3] == 'red':
            red = True
        elif in_obj < 1:
            red = False

        if char.isdigit() or (char == '-' and len(num) == 0):
            num = num + char
        elif len(num) > 1 or (len(num) > 0 and num != '-'):
            if in_obj > 0 and red is False:
                pending.append(int(num))
            elif red is True:
                pending = []
            elif in_obj < 1:
                pending.append(int(num))
                num_list.extend(pending)
            num = ''

    # return sum(num_list)
    return sum(num_list)