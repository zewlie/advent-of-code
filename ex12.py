"""Advent of Code: Day 12"""

def read_file(file):
    with open(file) as file:
        json = file.read().replace('\n', '')
    return json

def sum_nums(json):
    """Sum all numbers in string; ignore other content."""
    num_list = []
    num = ''

    for char in json:
        if char.isdigit() or char =='-' and len(num) == 0:
            num = char
        elif char.isdigit() or char =='-':
            num = num + char
        else:
            if len(num) > 0 and num != '-':
                num_list.append(int(num))
            elif len(num) > 1:
                num_list.append(int(num))
            num = ''

    return sum(num_list)
