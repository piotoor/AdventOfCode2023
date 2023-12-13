
def parse_day10_a():
    with open("day10.txt", "r") as f:
        data = list(f.read().splitlines())

    return data


def find_start(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                return i, j


go_up_set = {'|', '7', 'F'}
go_down_set = {'|', 'L', 'J'}
go_left_set = {'-', 'F', 'L'}
go_right_set = {'-', '7', 'J'}

dirs = {(1, 0): go_down_set, (0, 1): go_right_set, (-1, 0): go_up_set, (0, -1): go_left_set}


def start_replacement(r, c, data):
    if r - 1 < 0 or r + 1 >= len(data) or c - 1 < 0 or c + 1 >= len(data[0]):
        return data[r][c]
    else:
        possible_dirs = set()               # clockwise from U
        if data[r - 1][c] in go_up_set:
            possible_dirs.add(0)
        if data[r + 1][c] in go_down_set:
            possible_dirs.add(2)
        if data[r][c - 1] in go_left_set:
            possible_dirs.add(3)
        if data[r][c + 1] in go_right_set:
            possible_dirs.add(1)

        if 0 in possible_dirs and 1 in possible_dirs:
            return "L"
        elif 0 in possible_dirs and 2 in possible_dirs:
            return "|"
        elif 0 in possible_dirs and 3 in possible_dirs:
            return "J"

        elif 2 in possible_dirs and 1 in possible_dirs:
            return "F"
        elif 2 in possible_dirs and 3 in possible_dirs:
            return "7"
        elif 1 in possible_dirs and 3 in possible_dirs:
            return "-"


def print_map(r, c, data):
    for i in range(len(data)):
        if i != r:
            print(data[i])
        else:
            new_row = data[r][:c] + "XXXXXXXXXXXXXXXXXXXX " + data[r][c + 1:]
            print(new_row)

    print()
    print()


def calc_num_of_steps(data):
    # for x in data:
    #     print(x)
    r, c = find_start(data)
    repl = start_replacement(r, c, data)
    data[r] = data[r][:c] + repl + data[r][c + 1:]

    # for x in data:
    #     print(x)

    possible_connections = {
        ("L", (-1, 0)): "|7F",
        ("L", (0, 1)): "-7J",
        ("L", (1, 0)): "",
        ("L", (0, -1)): "",

        ("F", (-1, 0)): "",
        ("F", (0, 1)): "-7J",
        ("F", (1, 0)): "|JL",
        ("F", (0, -1)): "",

        ("J", (-1, 0)): "|7F",
        ("J", (0, 1)): "",
        ("J", (1, 0)): "",
        ("J", (0, -1)): "-FL",

        ("7", (-1, 0)): "",
        ("7", (0, 1)): "",
        ("7", (1, 0)): "|JL",
        ("7", (0, -1)): "-FL",

        ("-", (-1, 0)): "",
        ("-", (0, 1)): "-J7",
        ("-", (1, 0)): "",
        ("-", (0, -1)): "-FL",

        ("|", (-1, 0)): "|F7",
        ("|", (0, 1)): "",
        ("|", (1, 0)): "|LJ",
        ("|", (0, -1)): "",
    }

    opposite_dir = {(1, 0): (-1, 0), (0, 1): (0, -1), (-1, 0): (1, 0), (0, -1): (0, 1), (0, 0): (0, 0)}
    prev_dir = (0, 0)
    steps = 0
    curr = [r, c]

    while True:
        for d in dirs:
            if 0 > curr[0] + d[0] > len(data) or 0 > curr[1] + d[1] > len(data[0]):
                continue
            next_square = data[curr[0] + d[0]][curr[1] + d[1]]
            curr_square = data[curr[0]][curr[1]]
            if next_square in possible_connections[(curr_square, d)] and d != opposite_dir[prev_dir]:
                curr[0] += d[0]
                curr[1] += d[1]
                prev_dir = d
                steps += 1
                break
        if curr == [r, c]:
            break

    return steps // 2


def day10_a():
    data = parse_day10_a()
    print("day10_a = {}".format(calc_num_of_steps(data)))
