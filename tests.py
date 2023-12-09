import day1
import day2
import day3
import day4
import day5
import unittest
from parameterized import parameterized
import sys
sys.setrecursionlimit(150000)


class Day1(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             "1abc2",
             "pqr3stu8vwx",
             'a1b2c3d4e5f',
             "treb7uchet"
         ], 142),
        ("day_1a",
         day1.parse_day1_a(), 55621)
    ])
    def test_sum_of_calibration_values(self, _, data, expected):
        self.assertEqual(expected, day1.sum_of_calibration_values(data))

    @parameterized.expand([
        ("example 1",
         [
             "two1nine",
             "eightwothree",
             "abcone2threexyz",
             "xtwone3four",
             "4nineeightseven2",
             "zoneight234",
             "7pqrstsixteen"
         ], 281),
        ("example 2",
         [
             "mxmkjvgsdzfhseightonetwoeight7",
             "3five4s84four9rtbzllggz",
         ], 87 + 39),
        ("day_1b",
         day1.parse_day1_a(), 53592)
    ])
    def test_sum_of_calibration_values_v2(self, _, data, expected):
        self.assertEqual(expected, day1.sum_of_calibration_values_v2(data))


class Day2(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
             [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
             [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
             [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
             [(6, 3, 1), (1, 2, 2)],
         ], 8),
        ("day_2a",
         day2.parse_day2_a(), 2268)
    ])
    def test_sum_of_valid_game_id(self, _, data, expected):
        self.assertEqual(expected, day2.sum_of_valid_game_id(data))

    @parameterized.expand([
        ("example 1",
         [
             [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
             [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
             [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
             [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
             [(6, 3, 1), (1, 2, 2)],
         ], 2286),
        ("day_2b",
         day2.parse_day2_a(), 63542)
    ])
    def test_sum_of_game_powers(self, _, data, expected):
        self.assertEqual(expected, day2.sum_of_game_powers(data))


class Day3(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             "467..114...",     # added . at the end of every row to simplify the alg
             "...*.......",
             "..35..633..",
             "......#....",
             "617*.......",
             ".....+.58..",
             "..592......",
             "......755..",
             "...$.*.....",
             ".664.598...",
         ], 4361),
        ("day_3a",
         day3.parse_day3_a(), 527446)
    ])
    def test_sum_of_valid_game_id(self, _, data, expected):
        self.assertEqual(expected, day3.sum_of_numbers(data))

    @parameterized.expand([
        ("example 1",
         [
             "467..114...",     # added . at the end of every row to simplify the alg
             "...*.......",
             "..35..633..",
             "......#....",
             "617*.......",
             ".....+.58..",
             "..592......",
             "......755..",
             "...$.*.....",
             ".664.598...",
         ], 467835),
        ("day_3a",
         day3.parse_day3_a(), 73201705)
    ])
    def test_sum_of_valid_game_id(self, _, data, expected):
        self.assertEqual(expected, day3.sum_of_gear_ratios(data))


class Day4(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             ((41, 48, 83, 86, 17), (83, 86,  6, 31, 17,  9, 48, 53)),
             ((13, 32, 20, 16, 61), (61, 30, 68, 82, 17, 32, 24, 19)),
             ((1, 21, 53, 59, 44), (69, 82, 63, 72, 16, 21, 14,  1)),
             ((41, 92, 73, 84, 69), (59, 84, 76, 51, 58,  5, 54, 83)),
             ((87, 83, 26, 28, 32), (88, 30, 70, 12, 93, 22, 82, 36)),
             ((31, 18, 13, 56, 72), (74, 77, 10, 23, 35, 67, 36, 11))
         ], 13),
        ("day_4a",
         day4.parse_day4_a(), 21105)
    ])
    def test_count_total_points(self, _, data, expected):
        self.assertEqual(expected, day4.count_total_points(data))

    @parameterized.expand([
        ("example 1",
         [
             ((41, 48, 83, 86, 17), (83, 86,  6, 31, 17,  9, 48, 53)),
             ((13, 32, 20, 16, 61), (61, 30, 68, 82, 17, 32, 24, 19)),
             ((1, 21, 53, 59, 44), (69, 82, 63, 72, 16, 21, 14,  1)),
             ((41, 92, 73, 84, 69), (59, 84, 76, 51, 58,  5, 54, 83)),
             ((87, 83, 26, 28, 32), (88, 30, 70, 12, 93, 22, 82, 36)),
             ((31, 18, 13, 56, 72), (74, 77, 10, 23, 35, 67, 36, 11))
         ], 30),
        ("day_4b",
         day4.parse_day4_a(), 5329815)
    ])
    def test_count_total_cards(self, _, data, expected):
        self.assertEqual(expected, day4.count_total_cards_wrapper(data))


class Day5(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
            [79, 14, 55, 13],   # seeds
            [                   # seed -> soil
                [50, 98, 2],
                [52, 50, 48]
            ],
            [                   # soil -> fertilizer
                [0, 15, 37],
                [37, 52, 2],
                [39, 0, 15]
            ],
            [                   # fertilizer -> water
                [49, 53, 8],
                [0, 11, 42],
                [42, 0, 7],
                [57, 7, 4]
            ],
            [                   # water -> light
                [88, 18, 7],
                [18, 25, 70]
            ],
            [                   # light -> temperature
                [45, 77, 23],
                [81, 45, 19],
                [68, 64, 13]
            ],
            [                   # temperature -> humidity
                [0, 69, 1],
                [1, 0, 69]
            ],
            [                   # humidity -> location
                [60, 56, 37],
                [56, 93, 4]
            ],
         ], 35),
        ("day5_a",
         day5.parse_day5_a(), 806029445)
    ])
    def test_find_lowest_location_number(self, _, data, expected):
        self.assertEqual(expected, day5.find_lowest_location_number(data))

    @parameterized.expand([
        ("example 1",
         [
            [79, 14, 55, 13],   # seeds
            [                   # seed -> soil
                [50, 98, 2],
                [52, 50, 48]
            ],
            [                   # soil -> fertilizer
                [0, 15, 37],
                [37, 52, 2],
                [39, 0, 15]
            ],
            [                   # fertilizer -> water
                [49, 53, 8],
                [0, 11, 42],
                [42, 0, 7],
                [57, 7, 4]
            ],
            [                   # water -> light
                [88, 18, 7],
                [18, 25, 70]
            ],
            [                   # light -> temperature
                [45, 77, 23],
                [81, 45, 19],
                [68, 64, 13]
            ],
            [                   # temperature -> humidity
                [0, 69, 1],
                [1, 0, 69]
            ],
            [                   # humidity -> location
                [60, 56, 37],
                [56, 93, 4]
            ],
         ], 46),
        # ("day5_b",
        #  day5.parse_day5_a(), 806029445)
    ])
    def test_find_lowest_location_number_ranges(self, _, data, expected):
        self.assertEqual(expected, day5.find_lowest_location_number_ranges(data))
