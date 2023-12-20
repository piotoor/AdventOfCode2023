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


def tilt_west(data):
    for i in range(0, len(data)):
        free_col = 0
        for j in range(len(data[i])):
            if data[i][j] == '.':
                if j == 0 or data[i][j - 1] != '.':
                    free_col = j
            elif data[i][j] == 'O':
                if j > 0 and data[i][j - 1] == '.':
                    data[i][free_col] = 'O'
                    data[i][j] = '.'
                    free_col += 1
            else:
                free_col = i + 1

    return data


def tilt_south(data):
    for j in range(len(data[0])):
        free_row = len(data) - 1
        for i in range(len(data) - 1, -1, -1):
            if data[i][j] == '.':
                if i == len(data) - 1 or data[i + 1][j] != '.':
                    free_row = i
            elif data[i][j] == 'O':
                if i + 1 < len(data) and data[i + 1][j] == '.':
                    data[free_row][j] = 'O'
                    data[i][j] = '.'
                    free_row -= 1
            else:
                free_row = i - 1

    return data


def tilt_east(data):
    for i in range(len(data)):
        free_col = len(data[i]) - 1
        for j in range(len(data[i]) - 1, -1, -1):
            if data[i][j] == '.':
                if j == len(data[i]) - 1 or data[i][j + 1] != '.':
                    free_col = j
            elif data[i][j] == 'O':
                if j + 1 < len(data[i]) and data[i][j + 1] == '.':
                    data[i][free_col] = 'O'
                    data[i][j] = '.'
                    free_col -= 1
            else:
                free_col = i - 1

    return data


def total_load(data):
    # for x in data:
    #     print(x)

    data = tilt_north(data)

    # print()
    # for x in data:
    #     print(x)

    ans = 0
    for j in range(len(data[0])):
        for i in range(0, len(data)):
            if data[i][j] == 'O':
                ans += len(data) - i

    return ans


def hash_board(data):
    ans = []
    for x in data:
        ans.append(tuple(x))

    return tuple(ans)


def total_load_cycles(data):
    h = {}
    num_of_iters = 1000000000
    s = -1
    b = -1
    for i in range(1, num_of_iters + 1):
        data = tilt_north(data)
        data = tilt_west(data)
        data = tilt_south(data)
        data = tilt_east(data)

        hashed_data = hash_board(data)

        if hashed_data in h:
            if s == -1:
                s = h[hashed_data]
                b = i
                break
        else:
            h[hashed_data] = i

    a = s - 1
    b = b - s - 2
    c = num_of_iters

    ans_idx = s + c - a - ((c - a) // b) * b
    # print(a, b, c, s, ans_idx)

    ans = 0
    for key, val in h.items():
        if val == ans_idx:
            # for x in key:
            #     print(x)
            for j in range(len(key[0])):
                for i in range(0, len(key)):
                    if key[i][j] == 'O':
                        ans += len(key) - i

    return ans


def day14_a():
    data = parse_day14_a()
    print("day14a = {}".format(total_load(data)))


def day14_b():
    data = parse_day14_a()
    print("day14b = {}".format(total_load_cycles(data)))
