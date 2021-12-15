import sys
import os.path as ospath
from collections import defaultdict


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = [int(n) for n in lines[0].split(",")]
    crab_locations = defaultdict(int)
    for n in numbers:
        crab_locations[n] += 1

    location_part1 = sorted(numbers)[len(numbers) // 2]
    location_part2 = sum(numbers) // len(numbers)

    fuel_part1 = 0
    fuel_part2 = 0

    for position, number in crab_locations.items():
        distance = abs(position - location_part1)
        fuel_part1 += number * distance

    for position, number in crab_locations.items():
        distance = abs(position - location_part2)
        fuel_part2 += number * (distance / 2) * (distance + 1)

    print(fuel_part1)
    print(int(fuel_part2))
