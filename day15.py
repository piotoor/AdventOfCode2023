def parse_day15_a():
    with open("day15.txt", "r") as f:
        data = f.read()

    return data.split(",")


def hash_seq(s):
    curr = 0

    for x in s:
        curr += ord(x)
        curr *= 17
        curr = curr % 256

    return curr


def sum_of_results(data):
    ans = 0

    for x in data:
        ans += hash_seq(x)

    return ans


def day15_a():
    data = parse_day15_a()
    print("day15a = {}".format(sum_of_results(data)))


def focusing_power(data):
    ans = 0
    boxes = [[] for _ in range(256)]

    for x in data:
        if x[-1] == '-':
            label = x[:-1]
            hashed = hash_seq(label)
            for i in range(len(boxes[hashed])):
                if boxes[hashed][i][0] == label:
                    del boxes[hashed][i]
                    break
        else:
            label = x[:-2]
            hashed = hash_seq(label)
            focal_length = x[-1]
            exists = False
            for i in range(len(boxes[hashed])):
                if boxes[hashed][i][0] == label:
                    boxes[hashed][i][1] = focal_length
                    exists = True
                    break
            if not exists:
                boxes[hashed].append([label, focal_length])

    for i in range(len(boxes)):
        row_sum = 0
        for j in range(len(boxes[i])):
            row_sum += (i + 1) * (j + 1) * int(boxes[i][j][1])

        ans += row_sum

    return ans


def day15_b():
    data = parse_day15_a()
    print("day15b = {}".format(focusing_power(data)))
