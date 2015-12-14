"""Advent of Code: Day 12"""

def read_file(file):
    with open(file) as file:
        json = file.read().replace('\n', '')
    return json

def sum_nums(json):
    """Sum all numbers in string; ignore other content."""
    num_list = []
    num = ''

    for i, char in enumerate(json):
        if i < len(json) - 2:
            if json[i:i+3] == 'red':
                print json[i:i+3], 'matched red'
        if char.isdigit() or char =='-' and len(num) == 0:
            num = num + char
        elif len(num) > 1 or len(num) > 0 and num != '-':
            num_list.append(int(num))
            num = ''

    # return sum(num_list)
    return sum(num_list)