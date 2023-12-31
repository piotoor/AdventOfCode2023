def parse_day22_a():
    with open("day22.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    for row in data:
        begin, end = row.split("~")
        # print((begin.split(",")))
        parsed.append((tuple(map(int, begin.split(","))), tuple(map(int, end.split(",")))))
        print(parsed[-1])
    return parsed


class Block:
    def __init__(self, start, end, curr_id):
        self.cubes = []
        self.curr_id = curr_id
        self.visible = True

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

    def can_fall(self, other_blocks):
        for other in other_blocks:
            if other.curr_id == self.curr_id:
                continue
            if other.visible:
                if self.is_blocked_by(other):
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


def count_disintegrateable_blocks(data):
    blocks = []
    curr_id = 0
    for x in data:
        s, e = x
        blocks.append(Block(s, e, curr_id))
        print("block {} = {}       {} -> {}".format(curr_id, blocks[-1].cubes, s, e))
        curr_id += 1

    blocks.sort(key=lambda bl: bl.lowest_z)
    # for x in blocks:
    #     print(x.cubes)
    # for b1 in blocks:
    #     if b1.can_fall(blocks):
    #         print("{} can fall".format(b1.curr_id))

    print("dropping down...")

    for b in blocks:
        b.drop(blocks)

    # settled = False
    # while not settled:
    #     for b in blocks:
    #         b.drop(blocks)
    #
    #     settled = all([x.can_fall(blocks) is False for x in blocks])

    print("----------------- output -----------------")
    for b in blocks:
        print("block {} = {}".format(b.curr_id, b.cubes))

    print("-----------------------")
    ans = 0

    blocks.sort(key=lambda bl: bl.lowest_z)

    for b in blocks:
        b.visible = False
        print("trying {}".format(b.curr_id))
        disintegrateable = True
        for o in blocks:
            if b.curr_id == o.curr_id:
                continue
            if o.can_fall(blocks):
                disintegrateable = False
                break

        if disintegrateable:
            print("can be disintegrated {}".format(b.curr_id))
            ans += 1
        b.visible = True




    return ans


def day22_a():
    data = parse_day22_a()
    print("day22_a = {}".format(count_disintegrateable_blocks(data)))
