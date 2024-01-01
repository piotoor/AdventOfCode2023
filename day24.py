import sys


def parse_day24_a():
    with open("day24.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        s, v = row.split(" @ ")
        parsed.append([list(map(int, s.split(", "))), list(map(int, v.split(", ")))])
        print(parsed[-1])
    return parsed


def in_the_future(x, row):
    s, v = row
    if v[0] > 0:    # right
        if x > s[0]:
            return True
    else:           # left
        if x < s[0]:
            return True

    return False


def count_intersections(data, lower_bound, upper_bound):
    a = []
    b = []
    for row in data:
        s, v = row
        a.append(v[1] / v[0])
        b.append(s[1] - a[-1] * s[0])

    ans = 0

    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            den = (a[i] - a[j])
            if den != 0:
                x_int = (b[j] - b[i]) / den
            else:
                x_int = sys.maxsize

            y_int = a[i] * x_int + b[i]
            print("{} and {} ---> x_int = {} y_int = {} ai = {} aj = {}".format(data[i], data[j], x_int, y_int, a[i], a[j]))

            if lower_bound<= y_int < upper_bound and lower_bound <= x_int < upper_bound and in_the_future(x_int, data[i]) and in_the_future(x_int, data[j]) and a[i] != a[j]:
                ans += 1

    return ans


def day24_a():
    data = parse_day24_a()
    print("day24_a = {}".format(count_intersections(data, 200000000000000, 400000000000000 + 1)))
