def parse_day16_a():
    with open("day16.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for x in data:
        parsed.append(x)

    return parsed


def traverse(data, visited, visited_with_dir, cx, cy, dx, dy, depth):
    r, c = cx, cy
    while True:
        r += dx
        c += dy

        if 0 > r or r >= len(data) or 0 > c or c >= len(data[0]):
            break

        # print("--" * depth + " {} {}".format((r, c), (dx, dy)))
        visited.add((r, c))
        if ((r, c), (dx, dy)) not in visited_with_dir:
            visited_with_dir.add(((r, c), (dx, dy)))
        else:
            return
        if data[r][c] == '.':
            continue
        elif data[r][c] == '7':  # \
            dx, dy = dy, dx

        elif data[r][c] == '/':
            dx, dy = -dy, -dx
        elif data[r][c] == '|':
            if dy != 0:
                dx, dy = -1, 0
                traverse(data, visited, visited_with_dir, r, c, 1, 0, depth + 1)
        else:  # -
            if dx != 0:
                dx, dy = 0, -1
                traverse(data, visited, visited_with_dir, r, c, 0, 1, depth + 1)

    return


def num_of_energized_tiles(data):
    visited = set()
    visited_with_dir = set()

    traverse(data, visited, visited_with_dir, 0, -1, 0, 1, 0)

    ans = 0

    # for i in range(len(data)):
    #     row = ""
    #     for j in range(len(data[i])):
    #         found = False
    #         for x in visited:
    #             curr, direction = x
    #             if curr == (i, j):
    #                 row += '#'
    #                 ans += 1
    #                 found = True
    #                 break
    #         if not found:
    #             row += '.'
    #     print(row)

    return len(visited)


def day16_a():
    data = parse_day16_a()
    print("day16a = {}".format(num_of_energized_tiles(data)))
