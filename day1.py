import re


def parse_day1_a():
    with open("day1.txt", "r") as f:
        data = list(f.read().splitlines())

    # for x in data:
    #     print(x)

    return data


def sum_of_calibration_values(data):
    ans = 0

    for x in data:
        digits = re.sub("[^0-9]", "", x)
        digits_int = int(digits[0] + digits[-1])
        # print(digits_int)
        ans += digits_int

    return ans


def sum_of_calibration_values_v2(data):
    string_digits = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9
    }

    ans = 0

    for x in data:
        digits_positions_first = {}
        digits_positions_last = {}
        for sd in string_digits:
            pos = x.find(sd)
            digits_positions_first[pos] = string_digits[sd]
            pos = x.rfind(sd)
            digits_positions_last[pos] = string_digits[sd]

        for d in range(0, 10):
            pos = x.find(str(d))
            digits_positions_first[pos] = d
            pos = x.rfind(str(d))
            digits_positions_last[pos] = d

        # print("{} {} {}".format(x, digits_positions_first, digits_positions_last))

        del digits_positions_first[-1]
        del digits_positions_last[-1]

        dpf = sorted(digits_positions_first.items())
        dpl = sorted(digits_positions_last.items())

        ans += int(str(dpf[0][1]) + str(dpl[-1][1]))

    return ans


def day1_a():
    data = parse_day1_a()
    print("day1_a = {}".format(sum_of_calibration_values(data)))


def day1_b():
    data = parse_day1_a()
    print("day1_b = {}".format(sum_of_calibration_values_v2(data)))
