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


gen_h = {}


def generate(left, right, right_idx, curr_idx, curr, tmp):
    if curr_idx == len(left):
        if right_idx == len(right):
            return 1
        else:
            return 0
    elif right_idx >= len(right) and left[curr_idx] == '#':
        return 0
    else:
        ans = 0
        if left[curr_idx] == '.':
            if curr == 0:
                ans += generate(left, right, right_idx, curr_idx + 1, curr, tmp + '.')
            elif curr != right[right_idx]:
                return ans
            else:
                ans += generate(left, right, right_idx + 1, curr_idx + 1, 0, tmp + '.')
        elif left[curr_idx] == '#':
            if curr < right[right_idx]:
                ans += generate(left, right, right_idx, curr_idx + 1, curr + 1, tmp + '#')
            else:
                return ans
        else:
            ans_2 = 0
            left[curr_idx] = '.'
            curr_key = (curr_idx, right_idx, curr)
            if curr_key not in gen_h:
                gen_h[curr_key] = generate(left, right, right_idx, curr_idx, curr, tmp)
            ans_1 = gen_h[curr_key]
            left[curr_idx] = '?'
            if right_idx < len(right):
                left[curr_idx] = '#'
                ans_2 = generate(left, right, right_idx, curr_idx, curr, tmp)
                left[curr_idx] = '?'

            ans += ans_1 + ans_2
        return ans


def calc_sum_of_possible_arrangements(data):
    ans = 0
    for row in data:
        gen_h.clear()
        left, right = row
        left_list = list(left)
        left_list.append('.')
        curr = generate(left_list, right, 0, 0, 0, "")
        ans += curr

    return ans


def calc_sum_of_possible_arrangements_extended(data):
    ans = 0
    for row in data:
        gen_h.clear()
        left, right = row
        left = left + "?" + left + "?" + left + "?" + left + "?" + left
        right = right * 5
        left_list = list(left)
        left_list.append('.')

        curr = generate(left_list, right, 0, 0, 0, "")
        ans += curr

    return ans


def day12_a():
    data = parse_day12_a()
    print("day12_a = {}".format(calc_sum_of_possible_arrangements(data)))


def day12_b():
    data = parse_day12_a()
    print("day12_b = {}".format(calc_sum_of_possible_arrangements_extended(data)))
