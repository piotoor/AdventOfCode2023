
def parse_day11_a():
    with open("day11.txt", "r") as f:
        data = list(f.read().splitlines())

    return data


def column_empty(data, c):
    for i in range(len(data)):
        if data[i][c] != '.':
            return False
    return True


def expand(data):
    expanded_rows = []

    is_column_empty = [column_empty(data, j) for j in range(len(data[0]))]

    for row in data:
        expanded_rows.append(row)
        if all([x == '.' for x in row]):
            expanded_rows.append(row)

    ans = []
    for row in expanded_rows:
        expanded_row = ""
        for j in range(len(row)):
            expanded_row += row[j]
            if is_column_empty[j]:
                expanded_row += row[j]
        ans.append(expanded_row)

    return ans


def get_galaxies_as_coords(data):
    ans = []

    for i in range(0, len(data)):
        for j in range(0, len(data[i])):
            if data[i][j] == '#':
                ans.append((i, j))

    return ans


def dist(a, b):
    return abs(a[1] - b[1]) + abs(a[0] - b[0])


def calc_sum_of_lengths(data, expand_factor):
    expanded_data = expand(data)
    # for x in expanded_data:
    #     print(x)

    galaxies = get_galaxies_as_coords(expanded_data)
    ans = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ans += dist(galaxies[i], galaxies[j])

    return ans


def calc_sum_of_lengths(data, expand_factor):
    expanded_data = expand(data)
    # for x in expanded_data:
    #     print(x)

    galaxies = get_galaxies_as_coords(expanded_data)
    ans = 0

    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            ans += dist(galaxies[i], galaxies[j])

    return ans


def day11_a():
    data = parse_day11_a()
    print("day11_b = {}".format(calc_sum_of_lengths(data, 2)))

