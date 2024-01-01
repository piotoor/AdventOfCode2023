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
        paths.add(tuple(curr_path))
        # print()
        return 1
    else:
        ans = 0
        for x in neighbours[curr]:
            if x not in visited:
                visited.add(x)
                curr_path.append(x)
                ans += dfs(x, target, neighbours, visited, curr_path, paths)
                curr_path.pop()
                visited.remove(x)

        return ans


def compute_neighbours(data):
    neighbours = {}

    for r in range(len(data)):
        for c in range(len(data[0])):
            curr = (r, c)
            if curr not in neighbours:
                neighbours[curr] = set()
            if data[r][c] == ">":
                neighbours[curr].add((r, c + 1))
            elif data[r][c] == "v":
                neighbours[curr].add((r + 1, c))
            elif data[r][c] == "<":  # can be deleted
                neighbours[curr].add((r, c - 1))
            elif data[r][c] == "^":  # can be deleted
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
    
    neighbours = compute_neighbours(data)
    # for n in neighbours:
    #     print(n, neighbours[n])
    # return -1
    visited = set()
    curr_path = []
    paths = set()
    ans = dfs(source, target, neighbours, visited, curr_path, paths)

    return max([len(p) for p in paths])


def day23_a():
    data = parse_day23_a()
    print("day23_a = {}".format(longest_hike(data)))
