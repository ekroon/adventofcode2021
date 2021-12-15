import sys
import os.path as ospath
from collections import deque


def neighbours(y, x, y_size, x_size):
    n = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            n.append(
                (y + i, x + j)
            ) if 0 <= y + i < y_size and 0 <= x + j < x_size else None
    return n


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    octopuses = []
    for line in lines:
        octopuses.append([int(number) for number in line])

    part1 = 0
    part2 = -1

    all_indexes = deque()
    for i in range(0, 10):
        for j in range(0, 10):
            all_indexes.append((i, j))

    for step in range(0, 1000):
        flashed = set()
        to_visit = deque(all_indexes)
        while to_visit:
            i, j = to_visit.popleft()
            if (i, j) not in flashed:
                new = octopuses[i][j] + 1
                octopuses[i][j] += 1
                if new > 9:
                    to_visit.extend(neighbours(i, j, 10, 10))
                    flashed.add((i, j))
                    if step < 100:
                        part1 += 1
        for (i, j) in flashed:
            octopuses[i][j] = 0
        if len(flashed) == 100:
            part2 = step + 1
            break

    print(part1)
    print(part2)
