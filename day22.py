def parse_day22_a():
    with open("day22.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        begin, end = row.split("~")
        # print((begin.split(",")))
        parsed.append((tuple(map(int, begin.split(","))), tuple(map(int, end.split(",")))))
        print(parsed[-1])
    return parsed


def count_disintegrateable_blocks(data):
    for x in data:
        print(x)
    return -1


def day22_a():
    data = parse_day22_a()
    print("day22_a = {}".format(count_disintegrateable_blocks(data)))
