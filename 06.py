import sys
import os.path as ospath
from collections import defaultdict


if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = lines[0].split(",")
    school = defaultdict(int)
    for n in numbers:
        n = int(n)
        school[n] += 1

    part1 = None
    for rounds in range (0, 256):
        new_school = defaultdict(int)
        new_school[6] = school[0]
        new_school[8] = school[0]
        for i in range(1, 9):
            new_school[i-1] += school[i]
        school = new_school
        if rounds == 80:
            part1 = school

    part1 = sum(part1.values())
    part2 = sum(school.values())
    print(part1)
    print(part2)
