import math


def parse_day8_a():
    with open("day8.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = [data[0]]

    for i in range(2, len(data)):
        row = data[i]
        parsed.append((row[0:3], row[7:10], row[12:15]))

    # for x in parsed:
    #     print(x)
    return parsed


def calc_num_of_steps(data):
    steps = 0

    d = {}
    cmd = data[0]
    for i in range(1, len(data)):
        d[data[i][0]] = (data[i][1], data[i][2])

    cmd_idx = 0
    curr_element = "AAA"
    test = list()
    while True:
        curr_cmd = cmd[cmd_idx]
        if curr_cmd == 'L':
            curr_element = d[curr_element][0]
        else:
            curr_element = d[curr_element][1]

        steps += 1
        if curr_element == 'ZZZ':
            break
        cmd_idx += 1
        if cmd_idx == len(cmd):
            cmd_idx = 0

    return steps


def day8_a():
    data = parse_day8_a()
    print("day8_a = {}".format(calc_num_of_steps(data)))


def calc_num_of_steps_simultaneous(data):
    d = {}
    cmd = data[0]
    for i in range(1, len(data)):
        d[data[i][0]] = (data[i][1], data[i][2])
    curr_elements = []
    steps_arr = []
    for x in d:
        if x[2] == "A":
            curr_elements.append(x)
            steps_arr.append(0)

    for i in range(len(curr_elements)):
        steps_arr[i] = 0
        cmd_idx = 0

        while True:
            curr_cmd = cmd[cmd_idx]
            if curr_cmd == 'L':
                curr_elements[i] = d[curr_elements[i]][0]
            else:
                curr_elements[i] = d[curr_elements[i]][1]

            steps_arr[i] += 1
            if curr_elements[i][2] == "Z":
                break

            cmd_idx += 1
            if cmd_idx == len(cmd):
                cmd_idx = 0

    return math.lcm(*steps_arr)


def day8_b():
    data = parse_day8_a()
    print("day8_b = {}".format(calc_num_of_steps_simultaneous(data)))
