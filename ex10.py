"Advent of Code: Day 10"

def look_and_say(num_str, iterations):
    """Returns the result of a given number of iterations of Look and Say.

    Look and Say is a game during which a string of numbers is given, and the next
    string produced by reading the string aloud and using that reading as the next string.

    For example:

        1 becomes 11 (1 copy of digit 1).
        11 becomes 21 (2 copies of digit 1).
        21 becomes 1211 (one 2 followed by one 1).
        1211 becomes 111221 (one 1, one 2, and two 1s).
        111221 becomes 312211 (three 1s, two 2s, and one 1).
    """

    counter = 0

    while counter < iterations:
        last_num = ''
        num_count = 0
        new_str = ''

        for i, num in enumerate(num_str):

            # Check if at end of string
            if i == len(num_str) - 1:
                # New num
                if last_num != num and last_num != '':
                    new_str = new_str + str(num_count) + str(last_num) + '1' + num
                # Num is only num in string
                elif last_num == '':
                    new_str = '1' + num
                # Same num as prior
                else:
                    num_count += 1
                    new_str = new_str + str(num_count) + str(last_num)
                # Finish with string to return
                num_str = new_str

            # If not at end of string
            else:
                # New num
                if last_num != num and last_num != '':
                    new_str = new_str + str(num_count) + str(last_num)
                # New num or first num
                if last_num != num or last_num == '':
                    last_num = num
                    num_count = 1
                # Same num as prior
                else:
                    num_count += 1

        counter += 1
    return num_str

def las_result_len(num_str, iterations):
    result = look_and_say(num_str, iterations)
    return len(result)

