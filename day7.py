def parse_day7_a():
    with open("day7.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = []

    for x in data:
        hand, bidding = x.split(" ")
        parsed.append((hand, int(bidding)))

    return parsed


def calc_hand_strength(hand):
    s = {}
    for x in hand:
        if x in s:
            s[x] += 1
        else:
            s[x] = 1

    if len(s) == 1:
        return 6                    # 5 of a kind
    elif len(s) == 2:
        if max(s.values()) == 4:
            return 5                # 4 of a kind
        else:
            return 4                # full house
    elif len(s) == 3:
        if max(s.values()) == 3:
            return 3                # 3 of a kind
        else:
            return 2                # 2 pairs
    elif len(s) == 4:
        return 1                # 1 pair
    else:
        return 0                # high card


card_strength = {
    '1': 0,
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    'J': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}

card_strength_with_joker = {
    'J': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'Q': 11,
    'K': 12,
    'A': 13
}


def calc_total_winnings(data):
    ans = 0
    data.sort(key=lambda h: (calc_hand_strength(h[0]), card_strength[h[0][0]], card_strength[h[0][1]], card_strength[h[0][2]], card_strength[h[0][3]], card_strength[h[0][4]]))

    for i in range(len(data)):
        ans += data[i][1] * (i + 1)

    return ans


def day7_a():
    data = parse_day7_a()
    print("day7_a = {}".format(calc_total_winnings(data)))


def calc_hand_strength_with_jokers(hand):
    s = {}
    for x in hand:
        if x in s:
            s[x] += 1
        else:
            s[x] = 1

    jokers = 0
    if 'J' in s and hand != "JJJJJ":
        jokers += s['J']
        del s['J']

        max_keys = []
        for k in s:
            if s[k] == max(s.values()):
                max_keys.append(k)

        max_keys.sort(key=lambda mk: card_strength_with_joker[k])
        s[max_keys[-1]] += jokers

    if len(s) == 1:
        return 6                    # 5 of a kind
    elif len(s) == 2:
        if max(s.values()) == 4:
            return 5                # 4 of a kind
        else:
            return 4                # full house
    elif len(s) == 3:
        if max(s.values()) == 3:
            return 3                # 3 of a kind
        else:
            return 2                # 2 pairs
    elif len(s) == 4:
        return 1                # 1 pair
    else:
        return 0                # high card


def calc_total_winnings_with_jokers(data):
    ans = 0

    data.sort(key=lambda h: (calc_hand_strength_with_jokers(h[0]), card_strength_with_joker[h[0][0]], card_strength_with_joker[h[0][1]], card_strength_with_joker[h[0][2]], card_strength_with_joker[h[0][3]], card_strength_with_joker[h[0][4]]))

    for i in range(len(data)):
        ans += data[i][1] * (i + 1)

    return ans


def day7_b():
    data = parse_day7_a()
    print("day7_b = {}".format(calc_total_winnings_with_jokers(data)))
