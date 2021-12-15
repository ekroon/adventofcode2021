import sys
import os.path as ospath
from collections import defaultdict

# x,y instructions
if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        points = set()
        while line := f.readline().strip():
            points.add(tuple(int(n) for n in line.split(",")))

        instructions = []
        while line := f.readline().strip():
            line = line.split()[-1]
            instruction = line.split("=")
            instructions.append((instruction[0], int(instruction[1])))

    paper = points.copy()
    papers = [paper]
    for instruction in instructions:
        direction = instruction[0]
        index = instruction[1]
        new_paper = set()
        for point in paper:
            x, y = point
            # folding index e.g. 7, means folding before that index, not after
            if direction == "x":
                x = 2 * index - x if x > index else x
            if direction == "y":
                y = 2 * index - y if y > index else y
            new_paper.add((x, y))
            paper = new_paper
            papers.append(paper)

    print(len(papers[0]))
    xs = sorted([x for x, y in paper])
    ys = sorted([y for x, y in paper])
    for y in range(ys[0] - 1, ys[-1] + 2):
        line = []
        for x in range(xs[0] - 1, xs[-1] + 2):
            line.append("#" if (x, y) in paper else ".")
        print("".join(line))
