def parse_day25_a():
    with open("day25.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        # print(row.split(": "))
        k, v_str = row.split(": ")
        v = v_str.split(" ")
        for x in v:
            parsed.append((k, x))

    for x in parsed:
        print(x)

    return parsed


def multiple_size_of_groups(data):
    return -1


def day25_a():
    data = parse_day25_a()
    print("day25_a = {}".format(multiple_size_of_groups(data)))
