def parse_day12_a():
    with open("day12.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        a, b = x.split(" ")
        parsed.append([a, tuple(eval(b))])

    for x in parsed:
        print(x)

    return parsed


def calc_sum_of_possible_arrangements(data):
    return 3


def day12_a():
    data = parse_day12_a()
    print("day12_a = {}".format(calc_sum_of_possible_arrangements(data)))
