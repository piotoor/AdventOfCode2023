
def parse_day3_a():
    with open("day3.txt", "r") as f:
        data = list(f.read().splitlines())

    for i in range(len(data)):
        data[i] += '.'

    # print(data)
    return data


def adjacent_to_symbol(row, lower_bound, upper_bound, data):
    # print("row = {} lb = {} ub = {}".format(row, lower_bound, upper_bound))

    if lower_bound > 0 and data[row][lower_bound - 1] not in "0123456789." or upper_bound < len(data[row]) and data[row][upper_bound] not in "0123456789.":
        return True

    # print("[{}; {})".format(max(lower_bound - 1, 0), min(upper_bound + 1, len(data[row]))))
    for j in range(max(lower_bound - 1, 0), min(upper_bound + 1, len(data[row]))):
        if row - 1 >= 0 and data[row - 1][j] not in "0123456789." or row + 1 < len(data) and data[row + 1][j] not in "0123456789.":
            return True

    return False


def sum_of_numbers(data):
    # for x in data:
    #     print(x)
    # print()

    ans = 0

    for i in range(len(data)):
        curr_num_str = ""
        lower_bound = 0
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                if curr_num_str == "":
                    lower_bound = j
                curr_num_str += data[i][j]
            else:
                if curr_num_str != "":
                    curr_num = int(curr_num_str)
                    curr_num_str = ""
                    if adjacent_to_symbol(i, lower_bound, j, data):
                        # print(curr_num)
                        # print("-----------------------")
                        ans += curr_num

    return ans


def day3_a():
    data = parse_day3_a()
    print("day3_a = {}".format(sum_of_numbers(data)))


def find_possible_gears(row, lower_bound, upper_bound, data):
    possible_gears = []

    if lower_bound > 0 and data[row][lower_bound - 1] == "*":
        possible_gears.append((row, lower_bound - 1))

    if upper_bound < len(data[row]) and data[row][upper_bound] == "*":
        possible_gears.append((row, upper_bound))

    for j in range(max(lower_bound - 1, 0), min(upper_bound + 1, len(data[row]))):
        if row - 1 >= 0 and data[row - 1][j] == "*":
            possible_gears.append((row - 1, j))
        if row + 1 < len(data) and data[row + 1][j] == "*":
            possible_gears.append((row + 1, j))

    return possible_gears


def sum_of_gear_ratios(data):
    # for x in data:
    #     print(x)
    # print()

    possible_gears = {}
    ans = 0

    for i in range(len(data)):
        curr_num_str = ""
        lower_bound = 0
        for j in range(len(data[i])):
            if data[i][j].isdigit():
                if curr_num_str == "":
                    lower_bound = j
                curr_num_str += data[i][j]
            else:
                if curr_num_str != "":
                    curr_num = int(curr_num_str)
                    curr_num_str = ""

                    curr_possible_gears = find_possible_gears(i, lower_bound, j, data)
                    for gear in curr_possible_gears:
                        if gear not in possible_gears:
                            possible_gears[gear] = [curr_num]
                        else:
                            possible_gears[gear].append(curr_num)

    # print("possible_gears -----------")
    # for x in possible_gears:
    #     print("{} {}".format(x, possible_gears[x]))
    #
    # print("num of possible gears  {}".format(len(possible_gears.keys())))
    for gear in possible_gears:
        if len(possible_gears[gear]) == 2:
            a, b = possible_gears[gear]
            ans += a * b

    return ans


def day3_b():
    data = parse_day3_a()
    print("day3_b = {}".format(sum_of_gear_ratios(data)))
