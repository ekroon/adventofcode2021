from collections import deque


def alternative_1():
    """
    Only check the beginning and the end, the middle will be the same for the window
    """
    with open("01.txt") as f:
        parsed = [int(s) for s in f]
    results = []
    for skip in [1, 3]:
        total = 0
        skipped = parsed[skip:]
        for (x, y) in zip(parsed, skipped):
            if x < y:
                total += 1
        results.append(total)
    return results


def alternative_2():
    """
    Build a window and sum it
    """
    with open("01.txt") as f:
        parsed = [int(s) for s in f]
    results = []
    for window_size in [1, 3]:
        previous = None
        total = 0
        window = deque(maxlen=window_size)
        for x in parsed:
            window.append(x)
            if len(window) == window_size:
                current = sum(window)
                if previous and current > previous:
                    total += 1
                previous = current

        results.append(total)
    return results


if __name__ == "__main__":
    increasing = 0
    previous = None
    with open("01.txt") as f:
        for s in f:
            current = int(s.strip())
            if previous and current > previous:
                increasing += 1
            previous = current

    print(increasing)

    previous = None
    increasing = 0
    with open("01.txt") as f:
        input = f.readlines()
        for i in range(2, len(input)):
            current = 0
            for s in [input[i - 2], input[i - 1], input[i]]:
                current = current + int(s.strip())
            if previous and current > previous:
                increasing = increasing + 1
            previous = current

    print(increasing)
    assert [1154, 1127] == alternative_1()
    assert [1154, 1127] == alternative_2()

# 1154
# 1127
