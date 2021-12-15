import sys
import os.path as ospath
from collections import defaultdict


def clamp(x, min, max):
    if x > max:
        return max
    elif x < min:
        return min
    return x


def solve1(lines):
    sea = defaultdict(int)
    for [[x1, y1], [x2, y2]] in lines:
        if x1 == x2:
            y1, y2 = sorted([y1, y2])
            for y in range(y1, y2 + 1):
                sea[(x1, y)] += 1
        elif y1 == y2:
            x1, x2 = sorted([x1, x2])
            for x in range(x1, x2 + 1):
                sea[(x, y1)] += 1
        else:
            step_x = 1 if x1 <= x2 else -1
            step_y = 1 if y1 <= y2 else -1
            for (x, y) in zip(
                range(x1, x2 + step_x, step_x), range(y1, y2 + step_y, step_y)
            ):
                sea[(x, y)] += 1

    return len([n for n in sea.values() if n > 1])


def solve2(lines):
    sea = defaultdict(int)
    for [[x1, y1], [x2, y2]] in lines:
        step_x = clamp(x2 - x1, -1, 1)
        step_y = clamp(y2 - y1, -1, 1)
        x, y = x1, y1
        sea[(x, y)] += 1
        while x != x2 or y != y2:
            x += step_x
            y += step_y
            sea[(x, y)] += 1

    return len([n for n in sea.values() if n > 1])


def filter_horizontal_vertical(line):
    [x1, y1], [x2, y2] = line
    return x1 == x2 or y1 == y2


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    lines = [
        [[int(pair) for pair in pairs.split(",")] for pairs in line.split(" -> ")]
        for line in lines
    ]

    lines_part1 = list(filter(filter_horizontal_vertical, lines))
    part1_solve1 = solve1(lines_part1)
    part1_solve2 = solve2(lines_part1)

    part2_solve1 = solve1(lines)
    part2_solve2 = solve2(lines)

    assert part1_solve1 == part1_solve2
    assert part2_solve1 == part2_solve2

    print(part1_solve1)
    print(part2_solve1)
