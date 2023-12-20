def parse_day14_a():
    with open("day14.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        parsed.append(list(x))

    return parsed


def tilt_north(data):
    for j in range(len(data[0])):
        free_row = 0
        for i in range(0, len(data)):
            if data[i][j] == '.':
                if i == 0 or data[i - 1][j] != '.':
                    free_row = i
            elif data[i][j] == 'O':
                if i > 0 and data[i - 1][j] == '.':
                    data[free_row][j] = 'O'
                    data[i][j] = '.'
                    free_row += 1
            else:
                free_row = i + 1

    return data


def tilt_south(data):
    for j in range(len(data[0])):
        free_row = len(data) - 1
        for i in range(len(data) - 1, -1, -1):
            if data[i][j] == '.':
                if i == len(data) - 1 or data[i + 1][j] != '.':
                    free_row = i
            elif data[i][j] == 'O':
                if i + 1 < len(data) - 1 and data[i + 1][j] == '.':
                    data[free_row][j] = 'O'
                    data[i][j] = '.'
                    free_row -= 1
            else:
                free_row = i - 1

    return data


def tilt_north(data):
    for j in range(len(data[0])):
        free_row = 0
        for i in range(0, len(data)):
            if data[i][j] == '.':
                if i == 0 or data[i - 1][j] != '.':
                    free_row = i
            elif data[i][j] == 'O':
                if i > 0 and data[i - 1][j] == '.':
                    data[free_row][j] = 'O'
                    data[i][j] = '.'
                    free_row += 1
            else:
                free_row = i + 1

    return data


def total_load(data):
    for x in data:
        print(x)

    data = tilt_north(data)

    print()
    for x in data:
        print(x)

    ans = 0
    for j in range(len(data[0])):
        for i in range(0, len(data)):
            if data[i][j] == 'O':
                ans += len(data) - i

    return ans





def total_load_cycles(data):
    print("----------------------------------")
    for x in data:
        print(x)

    data = tilt_south(data)

    print()
    for x in data:
        print(x)
def day14_a():
    data = parse_day14_a()
    print("day14a = {}".format(total_load(data)))



def day14_b():
    data = parse_day14_a()
    print("day14b = {}".format(total_load_cycles(data)))
