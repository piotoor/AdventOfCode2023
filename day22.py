from collections import deque


def parse_day22_a():
    with open("day22.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        begin, end = row.split("~")
        parsed.append((tuple(map(int, begin.split(","))), tuple(map(int, end.split(",")))))
    return parsed


class Block:
    def __init__(self, start, end, curr_id):
        self.cubes = []
        self.curr_id = curr_id
        self.visible = True
        self.top_neighbours = set()
        self.bottom_neighbours = set()

        if start[0] != end[0]:
            for i in range(start[0], end[0] + 1):
                self.cubes.append([i, start[1], start[2]])
        elif start[1] != end[1]:
            for i in range(start[1], end[1] + 1):
                self.cubes.append([start[0], i, start[2]])
        else:
            for i in range(start[2], end[2] + 1):
                self.cubes.append([start[0], start[1], i])

        self.lowest_z = min(x[2] for x in self.cubes)

    def can_fall(self):
        for ngh in self.bottom_neighbours:
            if ngh.visible:
                if self.is_blocked_by(ngh):
                    return False
        return all(x[2] != 1 for x in self.cubes)

    def drop(self, other_blocks):
        new_z = 1

        for other in other_blocks:
            if other.curr_id == self.curr_id:
                continue
            if other.visible:
                for cube in self.cubes:
                    for other_cube in other.cubes:
                        if cube[0] == other_cube[0] and cube[1] == other_cube[1] and self.lowest_z > other_cube[2]:
                            new_z = max(new_z, other_cube[2] + 1)

        delta = self.lowest_z - new_z
        for x in self.cubes:
            x[2] -= delta

    def is_blocked_by(self, other):
        if other.visible and other.curr_id != self.curr_id:
            for c in self.cubes:
                for d in other.cubes:
                    if c[2] - 1 == d[2] and c[0] == d[0] and c[1] == d[1]:
                        return True
        return False


def count_blocks(data):
    blocks = []
    curr_id = 0
    for x in data:
        s, e = x
        blocks.append(Block(s, e, curr_id))
        # print("block {} = {}       {} -> {}".format(curr_id, blocks[-1].cubes, s, e))
        curr_id += 1

    blocks.sort(key=lambda bl: bl.lowest_z)

    # print("dropping down...")
    for b in blocks:
        b.drop(blocks)
    # print("dropping done")

    # print("----------------- output -----------------")
    # for b in blocks:
    #     print("block {} = {}".format(b.curr_id, b.cubes))

    ans_part1 = 0
    blocks.sort(key=lambda bl: bl.lowest_z)

    for b in blocks:
        for bb in blocks:
            if b is not bb:
                if b.is_blocked_by(bb):
                    b.bottom_neighbours.add(bb)
                    bb.top_neighbours.add(b)

    for i in range(len(blocks)):
        blocks[i].visible = False
        disintegrateable = True

        for ngh in blocks[i].top_neighbours:
            if ngh.can_fall():
                disintegrateable = False
                break

        if disintegrateable:
            ans_part1 += 1
        blocks[i].visible = True

    # print("top neighbours")
    # for b in blocks:
    #     print("block {}".format(b.curr_id))
    #     for x in b.top_neighbours:
    #         print("---- {}".format(x.curr_id))

    ans_part2 = 0
    for b in blocks:
        b.visible = False
        qq = deque()
        chain_reaction = 0
        h = set()
        for ngh in b.top_neighbours:
            qq.append(ngh)
            h.add(ngh)

        while qq:
            curr = qq.popleft()
            h.remove(curr)
            if curr.can_fall():
                curr.visible = False
                chain_reaction += 1
                for n in curr.top_neighbours:
                    if n in h:
                        continue
                    qq.append(n)
                    h.add(n)
        for k in blocks:
            k.visible = True
        ans_part2 += chain_reaction

    return ans_part1, ans_part2


def day22_a():
    data = parse_day22_a()
    print("day22_a = {}".format(count_blocks(data)[0]))


def day22_b():
    data = parse_day22_a()
    print("day22_b = {}".format(count_blocks(data)[1]))
