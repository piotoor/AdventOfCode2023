import day1
import unittest
from parameterized import parameterized

# class Day1(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              [1000, 2000, 3000],
#              [4000],
#              [5000, 6000],
#              [7000, 8000, 9000],
#              [10000]
#          ], 24000),
#         ("day_1a",
#          day1.parse_day1_a(), 69693)
#     ])
#     def test_find_highest_calories_amount(self, _, data, expected):
#         self.assertEqual(expected, day1.find_highest_calories_amount(data))
#
#     @parameterized.expand([
#         ("example 2",
#          [
#              [1000, 2000, 3000],
#              [4000],
#              [5000, 6000],
#              [7000, 8000, 9000],
#              [10000]
#          ], 45000),
#         ("day_1b",
#          day1.parse_day1_a(), 200945)
#     ])
#     def test_find_the_sum_of_top_three(self, _, data, expected):
#         self.assertEqual(expected, day1.find_the_sum_of_top_three(data))