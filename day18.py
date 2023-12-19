from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
import numpy as np

def parse_day18_a():
    with open("day18.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        direction, steps, color = x.split(" ")
        parsed.append((direction, int(steps), color[2:8]))
        # print(parsed[-1])

    return parsed


def area(path):
    return abs(sum(path[i][0] * (path[i + 1][1] - path[i + 1][0] * path[i][1]) for i in range(0, len(path) - 1))) / 2.0


def print_(path):
    p = [['.' for _ in range(50)] for _ in range(50)]

    for e in path:
        x, y = e
        p[x + 10][y + 10] = 'X'

    for x in p:
        print(x)


def calc_capacity(data):
    x = 0
    y = 0
    path = [(x, y)]
    ans = 0
    per = 0
    for row in data:
        d, s, c = row
        # if d == "U":
        #     while s > 0:
        #         y += 1
        #         path.append((x, y))
        #         s -= 1
        # elif d == "R":
        #     while s > 0:
        #         x += 1
        #         path.append((x, y))
        #         s -= 1
        # elif d == "D":
        #     while s > 0:
        #         y -= 1
        #         path.append((x, y))
        #         s -= 1
        # else:
        #     while s > 0:
        #         x -= 1
        #         path.append((x, y))
        #         s -= 1

        if d == "U":
            y += s
        elif d == "R":
            x += s
        elif d == "D":
            y -= s
        else:
            x -= s
        per += s
        path.append((x, y))
        # print(path)

    # print_(path)
    polygon = Polygon(path)
    return int(polygon.area + per // 2 + 1)


def day18_a():
    data = parse_day18_a()
    print("day18_a = {}".format(calc_capacity(data)))
