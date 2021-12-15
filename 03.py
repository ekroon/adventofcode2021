import sys
import os.path as ospath
import math


def clamp(x, min, max):
    if x > max:
        return max
    elif x < min:
        return min
    return x


def bin_iter_to_int(iter, conversion=lambda x: x):
    return int("".join([str(conversion(x)) for x in iter]), 2)


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"
    print(infile)

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    parsed = [[1 if c == "1" else 0 for c in line] for line in lines]

    # part 1: count numbers up from half the number of lines
    counts = [-int(len(parsed) / 2)] * len(parsed[0])
    for binary in parsed:
        for number_idx, x in enumerate(binary):
            counts[number_idx] += x

    # part 1: clamp numbers between 0 and 1, negative becomes a 0 for more zeroes, positive a 1 for more 1s
    gamma = bin_iter_to_int(counts, lambda x: clamp(x, 0, 1))
    epsilon = bin_iter_to_int(
        counts, lambda x: 1 - clamp(x, 0, 1)
    )  # we swap 0s and 1s for least common bit
    print(gamma * epsilon)

    # part 2: we sort the list by current index and pick the middle for most common and swap 0s and 1s for co2
    step_configurations = [
        [list(parsed), lambda pick: pick],
        [list(parsed), lambda pick: 1 - pick],
    ]
    for number_idx in range(len(parsed[0])):
        for idx, (binaries, pick_fn) in enumerate(step_configurations):
            if len(binaries) > 1:
                binaries = sorted(binaries, key=lambda x: x[number_idx])
                pick = pick_fn(binaries[math.floor(len(binaries) / 2)][number_idx])
                step_configurations[idx][0] = [
                    binary for binary in binaries if binary[number_idx] == pick
                ]

    oxygen = bin_iter_to_int(step_configurations[0][0][0])
    co2 = bin_iter_to_int(step_configurations[1][0][0])
    print(oxygen * co2)
