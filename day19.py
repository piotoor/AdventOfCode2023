def parse_day19_a():
    with open("day19.txt", "r") as f:
        data = list(f.read().splitlines())

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

    return [workflows, ratings]


def sum_of_rating_numbers(data):
    workflows, ratings = data
    # print(workflows, ratings)
    ans = 0
    # x m a s
    for r in ratings:
        print("-----------------------------------")
        print("rating = {}".format(r))
        result = 'None'
        curr_workflow = "in"
        x, m, a, s = r
        print("xmas = {} {} {} {}".format(x, m, a, s))
        while result not in ("A", "R"):
            w = workflows[curr_workflow]
            print("workflow = {}".format(w))
            for cond in w:
                c, act = cond
                print(c, act)
                if c != '':
                    if eval(c):
                        if act in ("A", "R"):
                            result = act
                        else:
                            curr_workflow = act
                            print("curr workflow = {}".format(curr_workflow))
                        break
                else:
                    if act in ("A", "R"):
                        result = act
                    else:
                        curr_workflow = act
        print("result = {} ----------------------------------------------".format(result))
        if result == "A":
            ans += sum(r)
    return ans


def day19_a():
    data = parse_day19_a()
    print("day19a = {}".format(sum_of_rating_numbers(data)))


# def day19_b():
#     data = parse_day19_a()
#     print("day19b = {}".format((data)))
