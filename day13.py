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


def count_rows_above_vertical_axis(matrix):
    ans = 0

    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            if matrix[i] == matrix[j]:
                print("found equal rows {} vs {}".format(matrix[i], matrix[j]))
                delta = (j + i) // 2

                if (j + i) % 2 != 0:
                    r1 = delta
                    r2 = delta + 1
                    symmetry = True
                    print("checking symmetry:")
                    while r1 >= 0 and r2 < len(matrix):
                        print("{} vs {}".format(r1, r2))
                        if matrix[r1] != matrix[r2]:
                            symmetry = False
                            break
                        r1 -= 1
                        r2 += 1
                    if symmetry:
                        print(delta + 1)
                        ans = max(ans, delta + 1)
    return ans


def transpose_matrix(matrix):
    ans = []

    for j in range(len(matrix[0])):
        new_row = ""
        for i in range(len(matrix)):
            new_row += matrix[i][j]
        ans.append(new_row)

    for x in ans:
        print(x)

    return ans


def sum_of_notes(data):
    ans = 0

    for p in data:
        print("-----------------------")
        for x in p:
            print(x)

        print("--> rows")
        cnt = 100 * count_rows_above_vertical_axis(p)
        ans += cnt
        print(cnt)
        print("--> transposed rows")
        cnt = count_rows_above_vertical_axis(transpose_matrix(p))
        ans += cnt
        print(cnt)

    return ans


def day13_a():
    data = parse_day13_a()
    print("day13_a = {}".format(sum_of_notes(data)))
