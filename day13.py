def parse_day13_a():
    with open("day13.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []
    curr = []
    for x in data:
        if len(x) == 0:
            parsed.append(curr.copy())
            curr.clear()
        else:
            curr.append(x)

    # for x in parsed:
    #     for y in x:
    #         print(y)
    #     print()

    return parsed


def equal_except_n(a, b, expected_diff):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
        if diff > expected_diff:
            return False

    return diff <= expected_diff


def count_rows_above_vertical_axis(matrix, expected_diff, old=-1):
    ans = 0

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if equal_except_n(matrix[i], matrix[j], expected_diff):
                # print("found equal rows {} vs {}".format(matrix[i], matrix[j]))
                delta = (j + i) // 2

                if (j + i) % 2 != 0:
                    r1 = delta
                    r2 = delta + 1
                    symmetry = True
                    # print("checking symmetry:")
                    while r1 >= 0 and r2 < len(matrix):
                        # print("{} vs {}".format(r1, r2))
                        if not equal_except_n(matrix[r1], matrix[r2], expected_diff):
                            symmetry = False
                            break
                        r1 -= 1
                        r2 += 1
                    if symmetry:
                        # print(delta + 1)
                        if delta + 1 != old:
                            ans = delta + 1
    return ans


def transpose_matrix(matrix):
    ans = []

    for j in range(len(matrix[0])):
        new_row = ""
        for i in range(len(matrix)):
            new_row += matrix[i][j]
        ans.append(new_row)

    # for x in ans:
    #     print(x)

    return ans


def sum_of_notes(data):
    ans = 0

    for p in data:
        # for x in p:
        #     print(x)

        cnt = 100 * count_rows_above_vertical_axis(p, 0)
        ans += cnt
        if cnt == 0:
            cnt = count_rows_above_vertical_axis(transpose_matrix(p), 0)
            ans += cnt

    return ans


def day13_a():
    data = parse_day13_a()
    print("day13_a = {}".format(sum_of_notes(data)))


def sum_of_notes_v2(data):
    ans = 0

    for p in data:
        # print("-----------------------")
        # for x in p:
        #     print(x)
        old = count_rows_above_vertical_axis(p, 0)
        cnt = 100 * count_rows_above_vertical_axis(p, 1, old)
        ans += cnt
        if cnt == 0:
            old = count_rows_above_vertical_axis(transpose_matrix(p), 0)
            cnt = count_rows_above_vertical_axis(transpose_matrix(p), 1, old)
            ans += cnt

    return ans


def day13_b():
    data = parse_day13_a()
    print("day13_b = {}".format(sum_of_notes_v2(data)))
