import sys
import os.path as ospath
from collections import defaultdict


def done_or_store(store, value):
    if store:
        if value < store:
            return False, value
    else:
        return False, value
    return True, store


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = lines[0].split(",")
    crab_locations = defaultdict(int)
    for n in numbers:
        n = int(n)
        crab_locations[n] += 1

    lowest_part1 = None
    lowest_part2 = None
    part1_done = False
    part2_done = False
    min, max = min(crab_locations.keys()), max(crab_locations.keys())
    for location in range(min, max+1):
        if part1_done and part2_done:
            break
        fuel_part1 = 0
        fuel_part2 = 0
        for position, number in crab_locations.items():
            distance = abs(position - location)
            fuel_part1 += number * distance
            fuel_part2 += number * (distance / 2) * (distance + 1)
        part1_done, lowest_part1 = done_or_store(lowest_part1, fuel_part1)
        part2_done, lowest_part2 = done_or_store(lowest_part2, fuel_part2)

    print(lowest_part1)
    print(int(lowest_part2))

