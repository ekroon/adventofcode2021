import sys
import os.path as ospath
from collections import defaultdict

# ecfdbg decfba aegd fdcag fagecd gd gcafb efdac cbgeafd dfg | bgacf afdebc fceda cabfg

if __name__ == '__main__':
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    number_segments = {0: 'abcefg', 1: 'cf', 2: 'acdeg', 3: 'acdfg',
                       4: 'bcdf', 5: 'abdfg', 6: 'abdefg', 7: 'acf',
                       8: 'abcdefg', 9: 'abcdfg'}

    segment_counts = {num: len(segments) for num, segments in number_segments.items()}

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

        part1 = 0
        part2 = 0
        for line in lines:
            signals, value = line.split(" | ")
            signals = [set(signal) for signal in signals.split(" ")]
            mapping = {}
            for signal in signals:
                match len(signal):
                    case 2:
                        mapping[1] = signal
                    case 3:
                        mapping[7] = signal
                    case 4:
                        mapping[4] = signal
                    case 7:
                        mapping[8] = signal

            signals.remove(mapping[1])
            signals.remove(mapping[7])
            signals.remove(mapping[4])
            signals.remove(mapping[8])

            mapping[9] = [signal for signal in signals if len(signal) == 6 and signal | mapping[4] == signal][0]
            signals.remove(mapping[9])
            mapping[3] = [signal for signal in signals if len(signal) == 5 and signal | mapping[1] == signal][0]
            signals.remove(mapping[3])
            mapping[0] = [signal for signal in signals if len(signal) == 6 and signal | mapping[1] == signal][0]
            signals.remove(mapping[0])
            mapping[6] = [signal for signal in signals if len(signal) == 6][0]
            signals.remove(mapping[6])
            mapping[5] = [signal for signal in signals if signal | mapping[6] == mapping[6]][0]
            signals.remove(mapping[5])
            mapping[2] = signals[0]
            signals.remove(mapping[2])

            number = 0
            for digit in value.split(" "):
                digit = set(digit)
                if len(digit) in [2, 3, 4, 7]:
                    part1 += 1
                digit = [num for num,signal in mapping.items() if signal == digit][0]
                number *= 10
                number += digit
            part2 += number

        print(part1)
        print(part2)
