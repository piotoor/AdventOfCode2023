import copy


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
        # print("-----------------------------------")
        # print("rating = {}".format(r))
        result = 'None'
        curr_workflow = "in"
        x, m, a, s = r
        # print("xmas = {} {} {} {}".format(x, m, a, s))
        while result not in ("A", "R"):
            w = workflows[curr_workflow]
            # print("workflow = {}".format(w))
            for cond in w:
                c, act = cond
                # print(c, act)
                if c != '':
                    if eval(c):
                        if act in ("A", "R"):
                            result = act
                        else:
                            curr_workflow = act
                            # print("curr workflow = {}".format(curr_workflow))
                        break
                else:
                    if act in ("A", "R"):
                        result = act
                    else:
                        curr_workflow = act
        # print("result = {} ----------------------------------------------".format(result))
        if result == "A":
            ans += sum(r)
    return ans


def check_rating(x, m, a, s, workflows):
    result = 'None'
    curr_workflow = "in"
    # print("xmas = {} {} {} {}".format(x, m, a, s))
    while result not in ("A", "R"):
        w = workflows[curr_workflow]
        # print("workflow = {}".format(w))
        for cond in w:
            c, act = cond
            # print(c, act)
            if c != '':
                if eval(c):
                    if act in ("A", "R"):
                        result = act
                    else:
                        curr_workflow = act
                        # print("curr workflow = {}".format(curr_workflow))
                    break
            else:
                if act in ("A", "R"):
                    result = act
                else:
                    curr_workflow = act

    return result


left_to_idx = {
    'x': 0,
    'm': 1,
    'a': 2,
    's': 3
}


def merge_ranges(ranges):
    idx = 0
    ranges = list(map(list, ranges))
    ranges.sort()
    for i in range(1, len(ranges)):
        if ranges[idx][1] >= ranges[i][0]:
            ranges[idx][1] = max(ranges[idx][1], ranges[i][1])
        else:
            idx += 1
            ranges[idx] = ranges[i]

    ranges = list(map(list, ranges))
    return ranges[:idx + 1]


def ranges_intersection(a, b):          # returns intersection, rest
    inters = []
    rest_l = []
    rest_r = []

    if not (b[0] > a[1] or b[1] < a[0]):
        inters = [max(a[0], b[0]), min(a[1], b[1])]
        if inters[0] == inters[1]:
            inters = []
        if b[0] < a[0]:
            rest_l = [b[0], a[0]]
        if b[1] > a[1]:
            rest_r = [a[1], b[1]]
    else:
        rest_l = b

    return inters, rest_l, rest_r


def reverse_range(r):
    if r[0] == 1:
        return [r[1], 4001]
    else:
        return [1, r[0]]


def compute_ranges(states, curr_state_in, data, workflow, depth):
    print("-" * depth + "curr_state_in = {}".format(curr_state_in), workflow)
    ans = False
    if workflow == "A":
        states.append(copy.deepcopy(curr_state_in))
        print(curr_state_in)
        return True
    elif workflow == "R":
        return False
    else:
        prev_c = []
        curr_state = copy.deepcopy(curr_state_in)
        for row in data[workflow]:
            # print(row)
            c, a = row
            if c != '':
                var = c[0]
                operator = c[1]
                val = c[2:]
                idx = left_to_idx[var]
                if operator == "<":
                    curr_range = [1, int(val)]
                else:
                    curr_range = [int(val) + 1, 4001]

                # print("-" * depth + "curr_range = {} c = {} a = {}, curr_state = {} idx = {}".format(curr_range, c, a, curr_state, idx))
                new_curr_state = copy.deepcopy(curr_state)
                new_curr_state[idx] = ranges_intersection(new_curr_state[idx], curr_range)[0]
                reversed_curr_range = reverse_range(curr_range)
                print("-" * depth + "new_curr_state = {} curr_range = {} reversd_curr_range = {}".format(new_curr_state, curr_range, reversed_curr_range))

                ans = compute_ranges(states, new_curr_state, data, a, depth + 1)


                curr_state[idx] = ranges_intersection(curr_state[idx], reversed_curr_range)[0]
                print("-" * depth + "curr_state = {} idx = {} reversed_curr_range = {}".format(curr_state, idx, reversed_curr_range))
                print()
            else:
                print("-" * depth + "the last one curr_state = {} curr_range = {}".format(curr_state, curr_range))
                ans = compute_ranges(states, curr_state, data, a, depth + 1)
    return ans


def num_of_valid_ratings(data):
    ans = 0
    workflows, ratings = data

    curr_state = [[1, 4001], [1, 4001], [1, 4001], [1, 4001]]
    states = []

    compute_ranges(states, curr_state, data[0], "in", 0)

    print("---------------------- ans ----------------------")
    for state in states:
        # print(state)
        for i in range(len(state)):
            if len(state[i]) == 0:
                state[i] = [[1, 4001]]

        print(state)


    for state in states:
        ans += (state[0][1] - state[0][0]) * (state[1][1] - state[1][0]) * (state[2][1] - state[2][0]) * (state[3][1] - state[3][0])


    return ans


def day19_a():
    data = parse_day19_a()
    print("day19a = {}".format(sum_of_rating_numbers(data)))


def day19_b():
    data = parse_day19_a()
    print("day19b = {}".format(num_of_valid_ratings(data)))
