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

    ranges.sort()
    for i in range(1, len(ranges)):
        if ranges[idx][1] >= ranges[i][0]:
            ranges[idx][1] = max(ranges[idx][1], ranges[i][1])
        else:
            idx += 1
            ranges[idx] = ranges[i]

    return ranges[:idx + 1]


def vi(map_list, key):
    for m in map_list:
        if m[0] <= key < m[0] + m[2]:
            return m[1] + key - m[0]
    return key


def find_lowest_location_number_ranges(data):
    # format:
    # [dst, src, len]
    seeds, seed_to_soil, soil_to_fert, fert_to_wat, wat_to_light, light_to_temp, temp_to_humid, humid_to_loc = data

    location_values = []
    seeds_intervals = []
    for i in range(0, len(seeds), 2):
        seeds_intervals.append([seeds[i], seeds[i] + seeds[i + 1]])

    # seeds_intervals = [[6, 8], [1, 9], [2, 4], [4, 7]]
    print(seeds_intervals)
    seeds_intervals = merge_ranges(seeds_intervals)
    print()
    print(seeds_intervals)
    ans = sys.maxsize
    for interval in seeds_intervals:
        print("processing interval {}".format(interval))
        for x in range(interval[0], interval[1]):
            if x % 100000 == 0:
                print("processing seed {}".format(x))
            ans = min(ans, v(humid_to_loc, v(temp_to_humid, v(light_to_temp, v(wat_to_light, v(fert_to_wat,
                                                                                                       v(soil_to_fert,
                                                                                                         v(seed_to_soil,
                                                                                                           x))))))))

    return ans


def day5_b():
    data = parse_day5_a()
    print("day5_b = {}".format(find_lowest_location_number_ranges(data)))
