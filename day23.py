import heapq
import sys


def parse_day23_a():
    with open("day23.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        parsed.append(row)
    return parsed


class Node:
    def __init__(self, coords, dist):
        self.coords = coords
        self.dist = dist

    def __lt__(self, other):
        return self.dist < other.dist


def dfs(curr, target, neighbours, visited, curr_path, paths):
    # print(curr)
    if curr == target:
        # print(curr_path)
        # paths.add(tuple(curr_path))
        paths.add(curr_path)
        # print()
        return
    else:
        for x in neighbours[curr]:
            if x not in visited:
                visited.add(x)
                # curr_path.append(x)
                dfs(x, target, neighbours, visited, curr_path + 1, paths)
                # curr_path.pop()
                visited.remove(x)

        return


def compute_neighbours(data, slopes_enabled):
    neighbours = {}

    for r in range(len(data)):
        for c in range(len(data[0])):
            curr = (r, c)
            if data[r][c] == '#':
                continue
            if curr not in neighbours:
                neighbours[curr] = set()

            if data[r][c] == ">" and slopes_enabled:
                neighbours[curr].add((r, c + 1))
            elif data[r][c] == "v" and slopes_enabled:
                neighbours[curr].add((r + 1, c))
            elif data[r][c] == "<" and slopes_enabled:  # can be deleted
                neighbours[curr].add((r, c - 1))
            elif data[r][c] == "^" and slopes_enabled:  # can be deleted
                neighbours[curr].add((r - 1, c))
            else:
                for i in range(max(0, r - 1), min(r + 2, len(data))):
                    for j in range(max(0, c - 1), min(c + 2, len(data[0]))):
                        if (i == r and j == c) or (i != r and j != c) or data[i][j] == "#":
                            continue
                        neighbours[curr].add((i, j))

    return neighbours


def longest_hike(data):
    start_r = 0
    start_c = 1
    target_r = len(data) - 1
    target_c = len(data[0]) - 2
    source = (start_r, start_c)
    target = (target_r, target_c)
    
    neighbours = compute_neighbours(data, True)

    visited = set()
    curr_path = 0
    paths = set()
    dfs(source, target, neighbours, visited, curr_path, paths)

    return max(paths)


def day23_a():
    data = parse_day23_a()
    print("day23_a = {}".format(longest_hike(data)))


def longest_hike_v2(data):
    start_r = 0
    start_c = 1
    target_r = len(data) - 1
    target_c = len(data[0]) - 2
    source = (start_r, start_c)
    target = (target_r, target_c)

    neighbours = compute_neighbours(data, False)
    visited = set()
    curr_path = 0
    paths = set()
    dfs(source, target, neighbours, visited, curr_path, paths)

    return max(paths)

    # visited = set()
    # curr_path = 0
    # paths = set()
    # dfs(source, target, neighbours, visited, curr_path, paths)

    # return max(paths)


# def longest_hike_v2(data):
#     start_r = 0
#     start_c = 1
#     target_r = len(data) - 1
#     target_c = len(data[0]) - 2
#     source = (start_r, start_c)
#     target = (target_r, target_c)
#
#     neighbours = compute_neighbours(data)
#
#     cnt = 0
#     for n in neighbours:
#         if len(neighbours[n]) > 2:
#             cnt += 1
#             print(n)
#     print("cnt = {}".format(cnt))
#     return -1
#
#     # visited = set()
#     # curr_path = 0
#     # paths = set()
#     # dfs(source, target, neighbours, visited, curr_path, paths)
#
#     # return max(paths)


def day23_b():
    data = parse_day23_a()
    print("day23_b = {}".format(longest_hike_v2(data)))

