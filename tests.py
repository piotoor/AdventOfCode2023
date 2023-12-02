import day1
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
