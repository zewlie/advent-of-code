"""Advent of Code: Day 2"""

def wrapping_paper_file_to_list(gift_file):
    with open(gift_file) as file:
        gift_list = [line.rstrip('\n') for line in file]

    return gift_list


def wrapping_paper_req(gift_dimension_list):
    """Returns the sq. feet of paper required to wrap the gifts in the list provided.

    Each gift requires:
    - Enough paper to cover the surface area (2*l*w + 2*w*h + 2*h*l)
    - Extra paper equivalent to the area of the smallest side of the gift
    """

    total_sq_ft = 0

    for gift in gift_dimension_list:
        l, w, h = split_dimensions(gift)
        surface_area = (2*l*w) + (2*w*h) + (2*h*l)
        slack = min((l*w), (w*h), (h*l))

        total_sq_ft += surface_area + slack

    return total_sq_ft


def ribbon_req(gift_dimension_list):
    """Returns the length of ribbon (in ft) required to wrap the gifts in the list provided.

    Each gift requires:
    - Enough ribbon to wrap the smallest perimeter of any one of its faces
    - Extra ribbon equivalent to the volume of the gift (l*w*h)
    """

    total_ft = 0

    for gift in gift_dimension_list:
        l, w, h = split_dimensions(gift)
        volume = l*w*h
        perimeter = min((l+w), (w+h), (h+l)) * 2

        total_ft += volume + perimeter

    return total_ft


def split_dimensions(gift_dimensions):
    """Splits gift dimension string into length, width, height ints."""
    l, w, h = gift_dimensions.split("x")
    return int(l), int(w), int(h)


