import sys
import os.path as ospath
import math
from collections import deque, defaultdict
from heapq import heappush, heappop


def neighbours(grid, coord):
    ns = []
    y, x = coord
    for neighbour_coord in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
        cost = grid.get(neighbour_coord)
        if cost:
            ns.append((neighbour_coord, cost))
    return ns


def dijkstra(grid, start, end):
    visited = set()
    pq = []
    costs = defaultdict(lambda: math.inf)
    costs[start] = 0
    heappush(pq, (0, start))

    while pq:
        cost, coord = heappop(pq)
        if coord == end:
            return cost
        visited.add(coord)
        for new_coord, new_cost in neighbours(grid, coord):
            if new_coord in visited:
                continue

            new_cost = costs[coord] + new_cost
            if costs[new_coord] > new_cost:
                costs[new_coord] = new_cost
                heappush(pq, (new_cost, new_coord))

    assert False


if __name__ == "__main__":
    infile = sys.argv[1] if len(sys.argv) > 1 else ospath.splitext(__file__)[0] + ".txt"

    with open(infile) as f:
        lines = [line.strip() for line in f.readlines()]

    grid = {}
    for y, line in enumerate(lines):
        for x, n in enumerate(line):
            grid[(y, x)] = int(n)

    y_size = y + 1
    x_size = x + 1

    big_grid = {}
    for (y, x), n in grid.items():
        for i in range(0, 5):
            for j in range(0, 5):
                y_ = y + y_size * i
                x_ = x + x_size * j
                n_ = n + i + j
                while n_ > 9:
                    n_ -= 9
                big_grid[(y_, x_)] = n_

    big_y_size = y_size * 5
    big_x_size = x_size * 5

    for grid, coord in [
        (grid, (y_size - 1, x_size - 1)),
        (big_grid, (big_y_size - 1, big_x_size - 1)),
    ]:
        cost = dijkstra(grid, (0, 0), coord)
        print(cost)
