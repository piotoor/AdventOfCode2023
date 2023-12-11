import re
from functools import reduce


def parse_day6_a():
    with open("day6.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []

    for x in data:
        x = x.split(":")
        x = re.split(r'\s+', x[1].strip())
        parsed.append(tuple(map(int, x)))

    # print(parsed)
    return parsed


def calc_num_of_ways_of_beating_the_record(data):
    ans = [0 for _ in range(len(data[0]))]
    for i in range(len(data[0])):
        t = data[0][i]
        s = data[1][i]

        for t_charge in range(t + 1):
            v = t_charge
            dist = v * (t - t_charge)
            if dist > s:
                ans[i] += 1

    return reduce(lambda x, y: x * y, ans)


def day6_a():
    data = parse_day6_a()
    print("day6_a = {}".format(calc_num_of_ways_of_beating_the_record(data)))


def calc_num_of_ways_of_beating_the_record_v2(data):
    ans = 0
    t_str = ""
    s_str = ""
    for i in range(len(data[0])):
        t_str += str(data[0][i])
        s_str += str(data[1][i])

    t = int(t_str)
    s = int(s_str)

    for t_charge in range(t + 1):
        v = t_charge
        dist = v * (t - t_charge)
        if dist > s:
            ans += 1

    return ans


def day6_b():
    data = parse_day6_a()
    print("day6_b = {}".format(calc_num_of_ways_of_beating_the_record_v2(data)))
