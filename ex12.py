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
        if char.isdigit() and len(num) == 0:
            num = char
        elif char.isdigit():
            num = num + char
        else:
            if len(num) > 0:
                num_list.append(num)
                num = ''

    return num_list
