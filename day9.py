import numpy as np


def parse_day9_a():
    with open("day9.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        parsed.append(list(map(int, x.split(" "))))

    # for x in parsed:
    #     print(x)
    return parsed


def calc_sum_of_extrapolated_values(data):
    ans = 0

    for row in data:
        np_row = np.array(row)
        np_diff = np.diff(np_row)
        diffs = [np_diff]
        while not all([x == 0 for x in diffs[-1]]):
            diffs.append(np.diff(diffs[-1]))

        diffs = [np_row] + diffs
        for i in range(len(diffs) - 2, 0, -1):
            diffs[i - 1] = np.append(diffs[i - 1], diffs[i - 1][-1] + diffs[i][-1])

        ans += diffs[0][-1]

    return ans


def day9_a():
    data = parse_day9_a()
    print("day9_a = {}".format(calc_sum_of_extrapolated_values(data)))


def calc_sum_of_extrapolated_values_beginning(data):
    ans = 0

    for row in data:
        np_row = np.array(row)
        np_diff = np.diff(np_row)
        diffs = [np_diff]
        while not all([x == 0 for x in diffs[-1]]):
            diffs.append(np.diff(diffs[-1]))

        diffs = [np_row] + diffs
        for i in range(len(diffs) - 2, 0, -1):
            diffs[i - 1] = np.insert(diffs[i - 1], 0, diffs[i - 1][0] - diffs[i][0])

        ans += diffs[0][0]

    return ans


def day9_b():
    data = parse_day9_a()
    print("day9_b = {}".format(calc_sum_of_extrapolated_values_beginning(data)))


