def parse_day4_a():
    with open("day4.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []

    for row in data:
        card_id, card_data = row.split(":")

        winning, player = card_data.split("|")
        winning_list = []
        player_list = []
        for x in winning.split(" "):
            if x != "":
                winning_list.append(int(x))

        for x in player.split(" "):
            if x != "":
                player_list.append(int(x))

        # print("{}    {}".format(winning_list, player_list))

        parsed.append((tuple(winning_list), tuple(player_list)))

    # print(parsed)
    return parsed


def count_total_points(data):
    ans = 0

    for x in data:
        winning, player = x
        won = set(winning) & set(player)
        if len(won) != 0:
            ans += pow(2, len(won) - 1)

    return int(ans)


def day4_a():
    data = parse_day4_a()
    print("day4_a = {}".format(count_total_points(data)))


h = {}


def count_total_cards(data, lb, ub, d):
    # print("--" * d + "[{}; {})".format(lb, ub))
    ans = 0
    for i in range(lb, ub):
        winning, player = data[i]
        won = set(winning) & set(player)
        n = len(won)
        # print("--" * d + "intersect[{}] = {}".format(i, won))
        if i not in h:
            h[i] = count_total_cards(data, i + 1, i + 1 + n, d + 1)
        ans += 1 + h[i]
        # ans += 1 + count_total_cards(data, i + 1, i + 1 + n, d + 1)

    return ans


def count_total_cards_wrapper(data):
    h.clear()
    ans = count_total_cards(data, 0, len(data), 0)

    # for x in h:
    #     print("h[{}] = {}".format(x, h[x]))

    return ans


def day4_b():
    data = parse_day4_a()
    print("day4_b = {}".format(count_total_cards_wrapper(data)))
