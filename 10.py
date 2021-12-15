import sys
import os.path as ospath


def line_score(line):
    stack = []
    for char in line:
        match char:
            case "(":
                stack.append(")")
            case "[":
                stack.append("]")
            case "{":
                stack.append("}")
            case "<":
                stack.append(">")
            case _:
                if stack.pop() != char:
                    match char:
                        case ")":
                            return 3, stack
                        case "]":
                            return 57, stack
                        case "}":
                            return 1197, stack
                        case ">":
                            return 25137, stack
    return 0, stack


def stack_score(stack):
    total = 0
    while stack:
        c = stack.pop()
        total *= 5
        match c:
            case ")":
                total += 1
            case "]":
                total += 2
            case "}":
                total += 3
            case ">":
                total += 4
    return total


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    parsed = [line_score(line) for line in lines]
    stack_scores = [stack_score(line[1]) for line in parsed if line[0] == 0]
    stack_scores.sort()

    print(sum([line[0] for line in parsed]))
    print(stack_scores[(len(stack_scores) // 2)])
