import numpy as np


def parse_day21_a():
    with open("day21.txt", "r") as f:
        data = list(f.read().splitlines())

    return data


def find_start(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return i, j

    return -1, -1


def print_visited(data, visited):
    for i in range(len(data)):
        row = ""
        for j in range(len(data[i])):
            if (i, j) in visited:
                row += "O"
            else:
                row += data[i][j]

        print(row)


def dfs(data, r, c, s, h, v):
    if s == 0:
        if (r, c) not in v:
            v.add((r, c))
    else:
        for new_pos in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
            i, j = new_pos
            if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or data[i][j] not in "S.":
                continue

            key = (i, j, s - 1)
            if key not in h:
                dfs(data, i, j, s - 1, h, v)
                h.add(key)


def count_garden_plots(data, steps):
    # start_r, start_c = find_start(data)
    start_r = len(data) // 2
    start_c = len(data[0]) // 2
    # print(start_r, start_c)
    h = set()
    visited = set()
    dfs(data, start_r, start_c, steps, h, visited)

    # print()
    # print()
    # print_visited(data, visited)
    # return len(ans)
    return len(visited)


def day21_a():
    data = parse_day21_a()
    print("day21_a = {}".format(count_garden_plots(data, 64)))


def expand_board(data, side):
    new_data = []

    for row in data:
        new_data.append(row * side)

    return new_data * side


def count_garden_plots_v2(data, s):
    dir_max_steps = 65
    y = []
    for side in [1, 3, 5]:
        data_expanded = expand_board(data, side)
        curr_dir_max_steps = dir_max_steps * side + side // 2
        y.append(count_garden_plots(data_expanded, curr_dir_max_steps))

    p = (s - 65) // 131
    x_1 = 0
    y_1 = y[0]
    x_2 = 1
    y_2 = y[1]
    x_3 = 2
    y_3 = y[2]

    # y_1 = a*x_1^2 + b*x_1 + c
    c = y_1     # x_1 = 0, therefore a * x_1^2 and b * x_1 = 0 -> c = y_1

    aa = np.array([[x_2 ** 2, x_2], [x_3 ** 2, x_3]])
    bb = np.array([y_2 - c, y_3 - c])
    a, b = np.linalg.solve(aa, bb)

    return int(a * p * p + b * p + c)


def day21_b():
    data = parse_day21_a()
    print("day21_b = {}".format(count_garden_plots_v2(data, 26501365)))
