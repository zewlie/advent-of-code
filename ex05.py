"""Advent of Code: Day 5"""

def strings_file_to_list(strings_file):
    with open(strings_file) as file:
        strings_list = [line.rstrip('\n') for line in file]

    return strings_list


def num_nice_strings(strings_list):
    """Returns the number of nice strings in the provided list.

    A string is nice ONLY if:
        (1) It contains at least 3 vowels (duplicates accepted).
        (2) It contains at least one instance of the same letter twice in a row.
        (3) It does not contain any of the phrases in naughty_pairs.
    """

    vowels = set(['a', 'e', 'i', 'o', 'u'])
    naughty_pairs = set(['ab', 'cd', 'pq', 'xy'])
    num_nice = 0

    for string in strings_list:
        string_vowels = 0
        naughty = False
        nice = False

        # Check condition 3
        for pair in naughty_pairs:
            if string.find(pair) >= 0:
                naughty = True

        while naughty is False and nice is False:
            # Check condition 1
            for char in string:
                if char in vowels:
                    string_vowels += 1

            if string_vowels >= 3:
                # Check condition 2 & confirm string is nice if passed
                for i in range(0, len(string) - 1):
                    if string[i] == string[i + 1]:
                        nice = True

            # If we get here, string is naughty
            naughty = True

        # If string is nice, increment final nice count up by 1
        if nice is True:
            num_nice += 1

    return num_nice

def num_nice_strings_2(strings_list):
    """Returns the number of nice strings in the provided list.

    A string is nice ONLY if:
        (1) It contains a pair of chars that appears at least twice, overlapping prohibited.
            - e.g. "xyxy", "aabcdefgaa" = GOOD, "aaa" = BAD.
        (2) It contains at least one char that appears twice, sandwiching another char.
            - e.g. "xyx", "aaa"
    """

    num_nice = 0

    for string in strings_list:
        char_pairs_indexes = {}
        nice = False

        # Check condition 2
        for i in range(0, len(string) - 2):
            if string[i] == string[i + 2]:
                nice = True

        if nice is True:
            nice = False

            # Build dictionary to check condition 1
            for i in range(0, len(string) - 1):
                if char_pairs_indexes.get(string[i] + string[i + 1]):
                    char_pairs_indexes[string[i] + string[i + 1]].extend([i, i + 1])
                else:
                    char_pairs_indexes[string[i] + string[i + 1]] = [i, i + 1]

            # Check condition 1
            for pair in char_pairs_indexes:
                if len(char_pairs_indexes[pair]) >= 4:
                    if len(char_pairs_indexes[pair]) == len(set(char_pairs_indexes[pair])):
                        nice = True
                        print char_pairs_indexes[pair]

        if nice is True:
            num_nice += 1

    return num_nice










