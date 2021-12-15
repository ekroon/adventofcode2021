import sys
import os.path as ospath
from collections import defaultdict


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [tuple(line.strip().split("-")) for line in f.readlines()]

    graph = defaultdict(list)
    for (e1, e2) in lines:
        graph[e1].append(e2)
        graph[e2].append(e1)

    def step(edges, current, visited, steps, twice):
        visited = visited.union({current}) if current.islower() else visited
        steps = steps + [current]

        if current == "end":
            return 1

        if len(steps) > len(edges) * 2:
            raise ValueError("Cycle in edges?", steps)

        to_visit = [
            e
            for e in graph[current]
            if (twice and e not in visited) or (not twice and e != "start")
        ]
        total = 0
        for edge in to_visit:
            total += step(edges, edge, visited, steps, twice or (edge in visited))
        return total

    part1 = step(graph, "start", set(), [], True)
    print(part1)

    part2 = step(graph, "start", set(), [], False)
    print(part2)
