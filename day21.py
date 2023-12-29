def parse_day21_a():
    with open("day21.txt", "r") as f:
        data = list(f.read().splitlines())

    return data


def find_start(data):
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == 'S':
                return i, j

    return -1, -1


def print_visited(data, visited):
    for i in range(len(data)):
        row = ""
        for j in range(len(data[i])):
            if (i, j) in visited:
                row += "O"
            else:
                row += data[i][j]

        print(row)


# def dfs(data, r, c, s, h, v):
#     if s == 0:
#         if (r, c) not in v:
#             v.add((r, c))
#             return 1
#         else:
#             return 0
#     else:
#         ans = 0
#         for new_pos in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
#             i, j = new_pos
#             if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or data[i][j] not in "S.":
#                 continue
#
#             ans += dfs(data, i, j, s - 1, h, v)
#
#         return ans


def dfs(data, r, c, s, h, v):
    if s == 0:
        if (r, c) not in v:
            v.add((r, c))
    else:
        for new_pos in ((r, c - 1), (r, c + 1), (r - 1, c), (r + 1, c)):
            i, j = new_pos
            if i < 0 or i >= len(data) or j < 0 or j >= len(data[0]) or data[i][j] not in "S.":
                continue

            key = (i, j, s - 1)
            if key not in h:
                dfs(data, i, j, s - 1, h, v)
                h.add(key)


def count_garden_plots(data, steps):
    start_r, start_c = find_start(data)
    print(start_r, start_c)
    h = set()
    visited = set()
    dfs(data, start_r, start_c, steps, h, visited)
    print_visited(data, visited)
    # return len(ans)
    return len(visited)


def day21_a():
    data = parse_day21_a()
    print("day21_a = {}".format(count_garden_plots(data, 64)))
