import day1
import day2
import unittest
from parameterized import parameterized


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
