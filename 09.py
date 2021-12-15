import sys
import os.path as ospath
from functools import reduce


def neighbours(y, x, y_size, x_size):
    n = []
    for i in [-1, 1]:
        n.append((y, x + i)) if 0 <= x + i < x_size else None
        n.append((y + i, x)) if 0 <= y + i < y_size else None
    return n


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    numbers = []
    for line in lines:
        numbers.append([int(number) for number in line])

    low_parts = []
    y_size = len(numbers)
    x_size = len(numbers[0])
    for y in range(y_size):
        for x in range(x_size):
            current = numbers[y][x]
            lowest = True
            for cy, cx in neighbours(y, x, y_size, x_size):
                if lowest and current >= numbers[cy][cx]:
                    lowest = False
            if lowest:
                low_parts.append((y, x, current))

    basins = []
    for y, x, height in low_parts:
        seen = set()
        visit = [(y, x)]
        while visit:
            y, x = visit.pop()
            seen.add((y, x))
            for cy, cx in neighbours(y, x, y_size, x_size):
                if (cy, cx) not in seen and numbers[cy][cx] != 9:
                    visit.append((cy, cx))
        basins.append(seen)

    print(sum([height + 1 for (_y, _x, height) in low_parts]))
    print(
        reduce(
            lambda acc, n: acc * n, sorted([len(b) for b in basins], reverse=True)[:3]
        )
    )
