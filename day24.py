def parse_day24_a():
    with open("day24.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        s, v = row.split(" @ ")
        parsed.append([list(map(int, s.split(", "))), list(map(int, v.split(", ")))])
        print(parsed[-1])
    return parsed


def count_intersections(data, lower_bound, upper_bound):
    return -1


def day24_a():
    data = parse_day24_a()
    print("day24_a = {}".format(count_intersections(data, 200000000000000, 400000000000000)))
