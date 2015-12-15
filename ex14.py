"""Advent of Code: Day 14"""


def make_reindeer_dict(file):
    """Returns a dictionary representing reindeer's racing stats.

    The keys are the reindeers' names.
    The values are their stats in a list:

        * index 0 = max speed (km/s)
        * index 1 = time spent at max speed (s)
        * index 2 = time spent resting (s)
        * index 3 = total time in one fly-rest cycle (s)
    """

    with open(file) as file:
        reindeer = {}
        for line in file:
            line = line.split()
            reindeer[line[0]] = [int(line[3]),
                                int(line[6]),
                                int(line[13]),
                                int(line[6]) + int(line[13])
                                ]

    return reindeer


def find_fastest(file, time):
    """Returns a 2-tuple containing the best distance run during the time allotted
    and a list of the reindeer that achieved that distance (winners).
    """

    reindeer = make_reindeer_dict(file)
    distances = {}
    winners = []

    # Build out distances dict (will be used to determine winner(s))
    for name in reindeer:
        d, t, rest, len_cycle = reindeer[name]

        cycles = time / len_cycle
        # Calculate total distance for the fully-completed fly-rest cycles
        total = d * t * cycles
        # Calculate time left over after the last full fly-rest cycle
        remainder = time - (cycles * len_cycle)

        # Check if the reindeer was still flying during the remainder time
        if remainder > t:
            # If no, add one full cycle's worth of distance
            total += d * t
        else:
            # If yes, add only the distance covered during the remainder time
            total += d * remainder

        distances[name] = total

    best_dist = max(distances.values())

    # Build out list of winners
    for name in distances:
        if distances[name] == best_dist:
            winners.append(name)

    return (best_dist, winners)


def find_best_score(file, time):
    """Returns the highest score recieved by any reindeer during the time allotted.

    Score represents time spent in the lead; the winner will have spent the most
    time in the lead, even if he didn't run the greatest distance.
    """

    reindeer = make_reindeer_dict(file)
    scores = {}
    time_passed = 1

    # Build out scores dict with all reindeer starting at 0
    for name in reindeer:
        scores[name] = 0

    # Get winners for each time increment from find_fastest()
    while time_passed <= time:
        current_dist, current_winners = find_fastest(file, time_passed)
        # Increment score for each winner
        for name in current_winners:
            scores[name] += 1
        time_passed += 1

    return max(scores.values())
