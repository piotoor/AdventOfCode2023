import re
import sys


def parse_day2_a():
    with open("day2.txt", "r") as f:
        data = list(f.read().splitlines())

    parsed_data = []

    for row in data:
        game_id, game_data = row.split(":")
        turns = game_data.split(";")
        turns_data = []
        for t in turns:
            turn = t.split(",")
            # print(cubes)
            turn_data = [0, 0, 0]
            for cubes in turn:
                cube = cubes.strip().split(" ")
                if cube[1] == "red":
                    turn_data[0] = cube[0]
                elif cube[1] == "green":
                    turn_data[1] = cube[0]
                else:
                    turn_data[2] = cube[0]
            turns_data.append(tuple(turn_data))
        # print("----------------------")
        # print(turns_data)
        parsed_data.append(turns_data)
    # print(parsed_data)

    return parsed_data


NUM_OF_RED_CUBES = 12
NUM_OF_GREEN_CUBES = 13
NUM_OF_BLUE_CUBES = 14


def sum_of_valid_game_id(data):
    ans = 0

    for i in range(len(data)):
        game_valid = True
        for x in data[i]:
            if int(x[0]) > NUM_OF_RED_CUBES or int(x[1]) > NUM_OF_GREEN_CUBES or int(x[2]) > NUM_OF_BLUE_CUBES:
                game_valid = False

        if game_valid:
            ans += (i + 1)

    return ans


def sum_of_game_powers(data):
    ans = 0

    for i in range(len(data)):
        max_red = max_green = max_blue = 0
        for x in data[i]:
            max_red = max(max_red, int(x[0]))
            max_green = max(max_green, int(x[1]))
            max_blue = max(max_blue, int(x[2]))

        ans += max_red * max_green * max_blue

    return ans


def day2_a():
    data = parse_day2_a()
    print("day2_a = {}".format(sum_of_valid_game_id(data)))


def day2_b():
    data = parse_day2_a()
    print("day2_b = {}".format(sum_of_game_powers(data)))
