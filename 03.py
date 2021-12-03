if __name__ == '__main__':
    total = 0
    counter = [0 for _x in range(12)]
    with open("03.txt") as f:
        parsed = []
        for s in f:
            total += 1
            line = s.strip()
            idx = 0
            parsed_line = [int(s) for s in line]
            parsed.append(parsed_line)
            for n in line:
                match n:
                    case "1":
                        counter[idx] = counter[idx] + 1
                idx += 1

        zeros = [total - counter[idx] for idx in range(12)]
        ones = [counter[idx] for idx in range(12)]
        most = int("".join([str(int(one > zero)) for one, zero in zip(ones, zeros)]), 2)
        least = int("".join([str(int(one < zero)) for one, zero in zip(ones, zeros)]), 2)
        print(most * least)

    idx = 0
    lines = parsed[:]
    while len(lines) > 1:
        to_beat = len(lines) / 2
        ones = sum([line[idx] for line in lines])
        most = 1 if ones >= to_beat else 0
        lines = [line for line in lines if line[idx] == most]
        idx += 1
    oxygen = int("".join([str(n) for n in lines[0]]), 2)

    idx = 0
    lines = parsed[:]
    while len(lines) > 1:
        to_beat = len(lines) / 2
        ones = sum([line[idx] for line in lines])
        least = 1 if ones < to_beat else 0
        lines = [line for line in lines if line[idx] == least]
        idx += 1
    co2 = int("".join([str(n) for n in lines[0]]), 2)

    print(oxygen * co2)
