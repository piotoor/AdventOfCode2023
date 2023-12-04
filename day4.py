import re


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


def count_total_cards(data):
    for x in data:
        winning, player = x
        won = set(winning) & set(player)

        for


def day4_b():
    data = parse_day4_a()
    print("day4_b = {}".format(count_total_cards(data)))
