import sys
import os.path as ospath
import logging
import math

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


def add_number(a, b):
    return [(nested + 1, v) for nested, v in a + b]


def explode(a):
    exploded = False
    new = []
    idx = 0
    while idx < len(a):
        nested, value = a[idx]
        if not exploded and nested == 5:
            _, next_value = a[idx + 1]
            exploded = True
            if idx - 1 >= 0:
                new[idx - 1] = (new[idx - 1][0], new[idx - 1][1] + value)
            new.append((nested - 1, 0))
            if idx + 2 < len(a):
                new.append((a[idx + 2][0], a[idx + 2][1] + next_value))
            idx += 3
        else:
            new.append((nested, value))
            idx += 1
    return new, exploded


def split(a):
    has_split = False
    new = []
    idx = 0
    while idx < len(a):
        nested, value = a[idx]
        if not has_split and value >= 10:
            has_split = True
            new.append((nested + 1, math.floor(value / 2)))
            new.append((nested + 1, math.ceil(value / 2)))
        else:
            new.append((nested, value))
        idx += 1

    return new, has_split


def lower(a):
    lowered = False
    new = []
    idx = 0
    while idx < len(a):
        if not lowered and idx + 1 < len(a) and a[idx][0] == a[idx + 1][0]:
            lowered = True
            new.append((a[idx][0] - 1, 3 * a[idx][1] + 2 * a[idx + 1][1]))
            idx += 2
        else:
            new.append(a[idx])
            idx += 1
    return new, lowered


def magnitude(a):
    total = a[0]
    for number in a[1:]:
        total = add_number(total, number)
        repeat = True
        while repeat:
            total, repeat = explode(total)
            if not repeat:
                total, repeat = split(total)

    repeat = True
    while repeat:
        total, repeat = lower(total)

    return total[0][1]


def parse(f):
    with open(infile) as f:
        numbers = []
        for line in f.readlines():
            line = line.strip()
            number = []
            nested = 0
            for c in line:
                match c:
                    case ",":
                        pass
                    case "[":
                        nested += 1
                    case "]":
                        nested -= 1
                    case _:
                        number.append((nested, int(c)))
            numbers.append(number)
    return numbers


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    numbers = parse(infile)

    print(magnitude(numbers))

    part2 = 0
    i = 0
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if i == j:
                continue
            pair = [numbers[i], numbers[j]]
            part2 = max(part2, magnitude(pair))

    print(part2)
