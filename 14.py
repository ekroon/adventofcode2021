import sys
import os.path as ospath
from collections import defaultdict
from itertools import groupby

# x,y instructions
if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        polymer = f.readline().strip()
        f.readline()

        rules = {}
        for line in f.readlines():
            line = line.strip().split(" -> ")
            rules[line[0]] = line[1]

    pairs = defaultdict(int)
    for i in range(0, len(polymer) - 1):
        pairs[polymer[i] + polymer[i + 1]] += 1

    for step in range(0, 40):
        new_pairs = defaultdict(int)
        for pair, value in pairs.items():
            reaction1 = pair[0] + rules[pair]
            reaction2 = rules[pair] + pair[1]
            # Add 2 pairs and in the end only count first element of pair
            new_pairs[reaction1] += value
            new_pairs[reaction2] += value
        pairs = new_pairs
        if step == 10:
            part_1 = pairs

    for pairs in [part_1, pairs]:
        quantities = defaultdict(int)
        quantities[
            polymer[-1]
        ] += 1  # Add 1 for last element which wasn't first in pair
        for pair, value in pairs.items():
            quantities[pair[0]] += value  # Count first element
        quantities = sorted(quantities.values())

        print(quantities[-1] - quantities[0])
