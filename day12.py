def parse_day12_a():
    with open("day12.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        a, b = x.split(" ")
        parsed.append([a, tuple(eval(b))])

    # for x in parsed:
    #     print(x)

    return parsed


def generate(left, right, right_idx, curr_idx, curr):
    # print("right_idx = {} curr = {}".format(right_idx, curr))
    if right_idx == len(right):
        for i in range(len(left)):
            if left[i] == '#' and curr[i] != '#' or left[i] == '.' and curr[i] != '.':
                return 0
        # print(curr)
        return 1
    else:
        max_offset = len(left) - curr_idx - (sum(right[right_idx:]) + len(right[right_idx:]) - 1)
        # print("right_idx = {} max_offset = {}".format(right_idx, max_offset))
        ans = 0
        for i in range(curr_idx, curr_idx + max_offset + 1):
            new_curr = curr.copy()
            valid = True
            for j in range(i, i + right[right_idx]):
                new_curr[j] = '#'
                # if left[j] not in "?#":
                #     valid = False
                #     break
            # for j in range(0, i + right[right_idx]):
            #     if left[j] == "#" and new_curr[j] == '.':
            #         valid = False
            # if valid:
            ans += generate(left, right, right_idx + 1, i + right[right_idx] + 1, new_curr)

        return ans


def calc_sum_of_possible_arrangements(data):
    ans = 0
    for row in data:
        left, right = row
        # print("------------------------------")
        # print("left = {} right = {}".format(left, right))
        min_length = sum(right) + len(right) - 1
        max_length = len(left)
        generated = set()
        curr = ['.' for _ in left]
        ans += generate(left, right, 0, 0, curr)

    return ans


def day12_a():
    data = parse_day12_a()
    print("day12_a = {}".format(calc_sum_of_possible_arrangements(data)))
