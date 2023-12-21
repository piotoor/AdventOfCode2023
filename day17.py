import sys
import heapq


def parse_day17_a():
    with open("day17.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        parsed.append(list(map(int, list(x))))

    return parsed


UP = (-1, 0)
DOWN = (1, 0)
LEFT = (0, -1)
RIGHT = (0, 1)


class State:
    def __init__(self, coords, cost, direction, steps):
        self.coords = coords
        self.cost = cost
        self.direction = direction
        self.steps = steps
        self.hash = (self.coords, self.direction, self.steps)

    def __lt__(self, other):
        return (self.cost, self.steps) < (other.cost, other.steps)

    def print(self):
        print("coords = {} dist = {}, direction = {}, steps = {}".format(self.coords, self.cost,
                                                                         self.direction, self.steps))

    def dump_as_tuple(self):
        return self.coords, self.cost, self.direction, self.steps


perp_dirs = {
    UP: (LEFT, RIGHT),
    DOWN: (LEFT, RIGHT),
    LEFT: (UP, DOWN),
    RIGHT: (UP, DOWN)
}


def dijkstra(data, source, target):
    qq = []
    visited = set()
    heapq.heappush(qq, State(source, 0, RIGHT, 0))
    heapq.heappush(qq, State(source, 0, DOWN, 0))

    while len(qq) > 0:
        curr = heapq.heappop(qq)
        if curr.hash in visited:
            continue

        visited.add(curr.hash)

        coords, cost, d, s = curr.dump_as_tuple()

        if coords == target:
            return cost

        if s < 3:  # continue direction
            new_curr = (coords[0] + d[0], coords[1] + d[1])
            r, c = new_curr
            if 0 <= r < len(data) and 0 <= c < len(data[0]):
                heapq.heappush(qq, State(new_curr, cost + data[r][c], d, s + 1))

        # take two perpendicular directions
        new_dirs = perp_dirs[d]
        for nd in new_dirs:
            new_curr = (coords[0] + nd[0], coords[1] + nd[1])
            r, c = new_curr
            if 0 <= r < len(data) and 0 <= c < len(data[0]):
                heapq.heappush(qq, State(new_curr, cost + data[r][c], nd, 1))

    return -1


def least_heat_loss(data):
    source = (0, 0)
    target = (len(data) - 1, len(data[0]) - 1)

    ans = dijkstra(data, source, target)

    return ans


def day17_a():
    data = parse_day17_a()
    print("day17a = {}".format(least_heat_loss(data)))
