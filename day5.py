import itertools
import sys


def parse_day5_a():
    with open("day5.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed = [[], [], [], [], [], [], [], []]

    parsed_idx = 0

    for row in data:
        if row == "":
            parsed_idx += 1

        elif not row[0].isdigit():
            if parsed_idx == 0:
                parsed[parsed_idx] = (list(map(int, row[7:].split(" "))))
            else:
                continue
        else:
            parsed[parsed_idx].append(list(map(int, row.split(" "))))

    # for x in parsed:
    #     print()
    #     for y in x:
    #         print(y)

    return parsed


def v(map_list, key):
    for m in map_list:
        if m[1] <= key < m[1] + m[2]:
            return m[0] + key - m[1]
    return key


def find_lowest_location_number(data):
    # format:
    # [dst, src, len]
    seeds, seed_to_soil, soil_to_fert, fert_to_wat, wat_to_light, light_to_temp, temp_to_humid, humid_to_loc = data

    location_values = []

    for x in seeds:
        # print("processing seed {}".format(x))
        location_values.append(v(humid_to_loc, v(temp_to_humid, v(light_to_temp, v(wat_to_light, v(fert_to_wat, v(soil_to_fert, v(seed_to_soil, x))))))))

    return min(location_values)


def day5_a():
    data = parse_day5_a()
    print("day5_a = {}".format(find_lowest_location_number(data)))


def merge_ranges(ranges):
    idx = 0
    ranges = list(map(list, ranges))
    ranges.sort()
    for i in range(1, len(ranges)):
        if ranges[idx][1] >= ranges[i][0]:
            ranges[idx][1] = max(ranges[idx][1], ranges[i][1])
        else:
            idx += 1
            ranges[idx] = ranges[i]

    ranges = tuple(map(tuple, ranges))
    return ranges[:idx + 1]


def convert_row_to_intervals(mp):
    ans = []

    for row in mp:
        dst, src, num = row
        ans.append(((src, src + num), dst - src))

    return tuple(ans)


def convert_seeds_to_intervals(seeds):
    # ans = []
    #
    # for i in range(0, len(seeds), 2):
    #     ans.append((seeds[i], seeds[i] + seeds[i + 1]))
    #
    # return ans

    return set((seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2))


def ranges_intersection(a, b):          # returns intersection, rest
    inters = ()
    rest_l = ()
    rest_r = ()

    if not (b[0] > a[1] or b[1] < a[0]):
        inters = (max(a[0], b[0]), min(a[1], b[1]))
        if inters[0] == inters[1]:
            inters = ()
        if b[0] < a[0]:
            rest_l = (b[0], a[0])
        if b[1] > a[1]:
            rest_r = (a[1], b[1])
    else:
        rest_l = b

    return inters, rest_l, rest_r


def find_lowest_location_number_ranges(data):
    # format:
    # [dst, src, len]
    seeds, seed_to_soil, soil_to_fert, fert_to_wat, wat_to_light, light_to_temp, temp_to_humid, humid_to_loc = data

    curr_ranges = set(merge_ranges(convert_seeds_to_intervals(seeds)))
    converted_maps = []
    for x in data[1:]:
        curr_map = convert_row_to_intervals(x)
        converted_maps.append(curr_map)

    for m in converted_maps:
        inters = set()
        for r in m:
            rests = set()
            for lr in curr_ranges:
                inter, rest_l, rest_r = ranges_intersection(r[0], lr)
                if len(inter) > 0:
                    inters.add((inter[0] + r[1], inter[1] + r[1]))
                if len(rest_l) > 0:
                    rests.add(rest_l)
                if len(rest_r) > 0:
                    rests.add(rest_r)

            curr_ranges = rests.copy()
            curr_ranges = set(merge_ranges(curr_ranges))

        curr_ranges |= inters
        curr_ranges = set(merge_ranges(curr_ranges))

    return min(curr_ranges)[0]


def day5_b():
    data = parse_day5_a()
    print("day5_b = {}".format(find_lowest_location_number_ranges(data)))
