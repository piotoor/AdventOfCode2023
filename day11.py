
def parse_day11_a():
    with open("day11.txt", "r") as f:
        data = list(f.read().splitlines())

    return data


def column_empty(data, c):
    for i in range(len(data)):
        if data[i][c] != '.':
            return False
    return True


def get_galaxies_as_coords(data, expand_factor, empty_cols, empty_rows):
    ans = []
    row_offset = 0
    for i in range(0, len(data)):
        col_offset = 0
        if empty_rows[i]:
            row_offset += expand_factor - 1
            continue
        for j in range(0, len(data[i])):
            if data[i][j] == '#':
                ans.append((i + row_offset, j + col_offset))
            elif empty_cols[j]:
                col_offset += expand_factor - 1

    return ans


def dist(a, b):
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


# def calc_sum_of_lengths(data, expand_factor):
#     expanded_data = expand(data)
#     # for x in expanded_data:
#     #     print(x)
#
#     galaxies = get_galaxies_as_coords(expanded_data)
#     ans = 0
#
#     for i in range(len(galaxies)):
#         for j in range(i + 1, len(galaxies)):
#             ans += dist(galaxies[i], galaxies[j])
#
#     return ans


def calc_sum_of_lengths(data, expand_factor):
    is_column_empty = [column_empty(data, j) for j in range(len(data[0]))]
    is_row_empty = [all([x == '.' for x in row]) for row in data]
    galaxies = get_galaxies_as_coords(data, expand_factor, is_column_empty, is_row_empty)
    ans = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ans += dist(galaxies[i], galaxies[j])

    return ans


def day11_a():
    data = parse_day11_a()
    print("day11_a = {}".format(calc_sum_of_lengths(data, 2)))


def day11_b():
    data = parse_day11_a()
    print("day11_b = {}".format(calc_sum_of_lengths(data, 1000000)))
