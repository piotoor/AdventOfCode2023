def parse_day19_a():
    with open("day19.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    first_part = True
    workflows = {}
    ratings = []
    for x in data:
        if x == '':
            first_part = False
            continue
        if first_part:
            pos = x.find("{")
            label = x[:pos]
            conditions = x[pos + 1:-1].split(",")
            conditions_parsed = []
            for xx in conditions:
                if ":" in xx:
                    conditions_parsed.append(tuple(xx.split(":")))
                else:
                    conditions_parsed.append(("", xx))
            workflows[label] = tuple(conditions_parsed)
        else:
            ratings_row = x[1: -1].split(",")
            ratings.append([])
            for r in ratings_row:
                ratings[-1].append(int(r[2:]))

    for x in workflows:
        print(x, workflows[x])

    for y in ratings:
        print(y)

    return parsed


def sum_of_rating_numbers(data):
    return -1


def day19_a():
    data = parse_day19_a()
    print("day19a = {}".format(sum_of_rating_numbers(data)))


# def day19_b():
#     data = parse_day19_a()
#     print("day19b = {}".format((data)))
