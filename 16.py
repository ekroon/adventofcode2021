import sys
import os.path as ospath
import math
import logging

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)

VERSION_NUMBER_TOTAL = 0


def int_list_to_digit(l):
    return int("".join(l), 2)


def handle_packet_type(packet_type, values):
    match packet_type:
        case 0:
            return sum(values)
        case 1:
            return math.prod(values)
        case 2:
            return min(values)
        case 3:
            return max(values)
        case 5:
            assert len(values) == 2
            return 1 if values[0] > values[1] else 0
        case 6:
            assert len(values) == 2
            return 1 if values[0] < values[1] else 0
        case 7:
            assert len(values) == 2
            return 1 if values[0] == values[1] else 0


def parse_packet(binary, idx):
    version = int_list_to_digit(binary_input[idx : idx + 3])
    idx += 3
    packet_type = int_list_to_digit(binary_input[idx : idx + 3])
    idx += 3

    LOGGER.debug("VERSION: %s", version)
    LOGGER.debug("TYPE: %s", packet_type)
    global VERSION_NUMBER_TOTAL
    VERSION_NUMBER_TOTAL += version
    total = None
    match packet_type:
        case 4:  # literal_value
            new_index, value = parse_literal(binary_input, idx)
            idx = new_index
            total = value
        case _:
            new_index, values = parse_operator(binary_input, idx)
            idx = new_index
            total = handle_packet_type(packet_type, values)

    LOGGER.info("Total value for type (%s): %s", packet_type, total)

    assert total is not None
    return idx, total


def parse_literal(binary, idx):
    bits = []
    loop = 1
    while loop:
        loop -= 1
        loop += int_list_to_digit(binary[idx : idx + 1])
        idx += 1
        bits.extend(binary[idx : idx + 4])
        idx += 4
    return idx, int_list_to_digit(bits)


def parse_operator(binary, idx):
    length_type = int_list_to_digit(binary[idx : idx + 1])
    idx += 1

    values = []
    if length_type == 0:  # next 15 in bits
        length = int_list_to_digit(binary[idx : idx + 15])
        idx += 15
        stop_at = idx + length
        while idx < stop_at:
            idx, value = parse_packet(binary, idx)
            values.append(value)

    elif length_type == 1:  # next 11 in packets
        length = int_list_to_digit(binary[idx : idx + 11])
        idx += 11
        while length > 0:
            length -= 1
            idx, value = parse_packet(binary, idx)
            values.append(value)
    else:
        assert False

    return idx, values


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        line = [line.strip() for line in f.readlines()][0]

    binary_input = []
    for c in line:
        binary_input.extend(list(bin(int(c, 16))[2:].rjust(4, "0")))

    assert len(binary_input) == 4 * len(line)
    # print("BINARY LENGTH:", len(binary_input))
    _, part2 = parse_packet(binary_input, 0)

    print("PART1:", VERSION_NUMBER_TOTAL)
    print("PART2:", part2)
