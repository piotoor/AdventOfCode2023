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
    per = 0
    for row in data:
        d, s, c = row
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


def parse_day18_b():
    with open("day18.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        direction, steps, color = x.split(" ")
        new_steps = int(color[2:7], 16)
        new_dir_int = color[7:8]

        new_dir = ""
        if new_dir_int == '0':
            new_dir = "R"
        elif new_dir_int == '1':
            new_dir = "D"
        elif new_dir_int == '2':
            new_dir = "L"
        else:
            new_dir = "U"

        parsed.append((new_dir, new_steps))

    # for x in parsed:
    #     print(x)

    return parsed


def calc_capacity_v2(data):
    x = 0
    y = 0
    path = [(x, y)]
    per = 0
    for row in data:
        d, s = row
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


def day18_b():
    data = parse_day18_b()
    print("day18_b = {}".format(calc_capacity_v2(data)))
