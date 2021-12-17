import sys
import os.path as ospath
import logging

logging.basicConfig(level=logging.ERROR)
LOGGER = logging.getLogger(__name__)


def generate_x_steps(start_speed):
    speed = start_speed
    position = 0
    while True:
        position = position + speed
        yield position
        speed -= 1 if speed > 0 else 0


def generate_y_steps(start_speed, min_speed):
    speed = start_speed
    position = 0
    while speed >= min_speed:
        position = position + speed
        yield position
        speed -= 1


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        line = [line.strip() for line in f.readlines()][0]
        parts = line.split(" ")
        x_parts = parts[2][2:-1].split("..")
        y_parts = parts[3][2:].split("..")
        x_range = tuple(int(n) for n in x_parts)
        assert x_range[0] < x_range[1]
        y_range = tuple(int(n) for n in y_parts)
        assert y_range[0] < y_range[1]

    part1 = int(y_range[0] / 2 * (y_range[0] + 1))
    print(f"part1: {part1}")

    part2 = 0
    considered_locations = 0
    considered_speeds = 0
    for x_speed in range(0, x_range[1] + 1):
        for y_speed in range(y_range[0], -y_range[0]):
            considered_speeds += 1
            for x, y in zip(
                generate_x_steps(x_speed), generate_y_steps(y_speed, y_range[0])
            ):
                considered_locations += 1
                if x_range[0] <= x <= x_range[1] and y_range[0] <= y <= y_range[1]:
                    part2 += 1
                    break

    print(
        f"part2: {part2}, considered_speeds: {considered_speeds}, considered locations: {considered_locations}"
    )
