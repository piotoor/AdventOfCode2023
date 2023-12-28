import day1
import day2
import day3
import day4
import day5
import day6
import day7
import day8
import day9
import day10
import day11
import day12
import day13
import day14
import day15
import day16
import day17
import day18
import day19
import day20

import unittest
from parameterized import parameterized
import sys
sys.setrecursionlimit(150000)


# class Day1(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              "1abc2",
#              "pqr3stu8vwx",
#              'a1b2c3d4e5f',
#              "treb7uchet"
#          ], 142),
#         ("day_1a",
#          day1.parse_day1_a(), 55621)
#     ])
#     def test_sum_of_calibration_values(self, _, data, expected):
#         self.assertEqual(expected, day1.sum_of_calibration_values(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              "two1nine",
#              "eightwothree",
#              "abcone2threexyz",
#              "xtwone3four",
#              "4nineeightseven2",
#              "zoneight234",
#              "7pqrstsixteen"
#          ], 281),
#         ("example 2",
#          [
#              "mxmkjvgsdzfhseightonetwoeight7",
#              "3five4s84four9rtbzllggz",
#          ], 87 + 39),
#         ("day_1b",
#          day1.parse_day1_a(), 53592)
#     ])
#     def test_sum_of_calibration_values_v2(self, _, data, expected):
#         self.assertEqual(expected, day1.sum_of_calibration_values_v2(data))
#
#
# class Day2(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
#              [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
#              [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
#              [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
#              [(6, 3, 1), (1, 2, 2)],
#          ], 8),
#         ("day_2a",
#          day2.parse_day2_a(), 2268)
#     ])
#     def test_sum_of_valid_game_id(self, _, data, expected):
#         self.assertEqual(expected, day2.sum_of_valid_game_id(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              [(4, 0, 3), (1, 2, 6), (0, 2, 0)],
#              [(0, 2, 1), (1, 3, 4), (0, 1, 1)],
#              [(20, 8, 6), (4, 13, 5), (1, 5, 0)],
#              [(3, 1, 6), (6, 3, 0), (14, 3, 15)],
#              [(6, 3, 1), (1, 2, 2)],
#          ], 2286),
#         ("day_2b",
#          day2.parse_day2_a(), 63542)
#     ])
#     def test_sum_of_game_powers(self, _, data, expected):
#         self.assertEqual(expected, day2.sum_of_game_powers(data))
#
#
# class Day3(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              "467..114...",     # added . at the end of every row to simplify the alg
#              "...*.......",
#              "..35..633..",
#              "......#....",
#              "617*.......",
#              ".....+.58..",
#              "..592......",
#              "......755..",
#              "...$.*.....",
#              ".664.598...",
#          ], 4361),
#         ("day_3a",
#          day3.parse_day3_a(), 527446)
#     ])
#     def test_sum_of_valid_game_id(self, _, data, expected):
#         self.assertEqual(expected, day3.sum_of_numbers(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              "467..114...",     # added . at the end of every row to simplify the alg
#              "...*.......",
#              "..35..633..",
#              "......#....",
#              "617*.......",
#              ".....+.58..",
#              "..592......",
#              "......755..",
#              "...$.*.....",
#              ".664.598...",
#          ], 467835),
#         ("day_3a",
#          day3.parse_day3_a(), 73201705)
#     ])
#     def test_sum_of_valid_game_id(self, _, data, expected):
#         self.assertEqual(expected, day3.sum_of_gear_ratios(data))
#
#
# class Day4(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ((41, 48, 83, 86, 17), (83, 86,  6, 31, 17,  9, 48, 53)),
#              ((13, 32, 20, 16, 61), (61, 30, 68, 82, 17, 32, 24, 19)),
#              ((1, 21, 53, 59, 44), (69, 82, 63, 72, 16, 21, 14,  1)),
#              ((41, 92, 73, 84, 69), (59, 84, 76, 51, 58,  5, 54, 83)),
#              ((87, 83, 26, 28, 32), (88, 30, 70, 12, 93, 22, 82, 36)),
#              ((31, 18, 13, 56, 72), (74, 77, 10, 23, 35, 67, 36, 11))
#          ], 13),
#         ("day_4a",
#          day4.parse_day4_a(), 21105)
#     ])
#     def test_count_total_points(self, _, data, expected):
#         self.assertEqual(expected, day4.count_total_points(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ((41, 48, 83, 86, 17), (83, 86,  6, 31, 17,  9, 48, 53)),
#              ((13, 32, 20, 16, 61), (61, 30, 68, 82, 17, 32, 24, 19)),
#              ((1, 21, 53, 59, 44), (69, 82, 63, 72, 16, 21, 14,  1)),
#              ((41, 92, 73, 84, 69), (59, 84, 76, 51, 58,  5, 54, 83)),
#              ((87, 83, 26, 28, 32), (88, 30, 70, 12, 93, 22, 82, 36)),
#              ((31, 18, 13, 56, 72), (74, 77, 10, 23, 35, 67, 36, 11))
#          ], 30),
#         ("day_4b",
#          day4.parse_day4_a(), 5329815)
#     ])
#     def test_count_total_cards(self, _, data, expected):
#         self.assertEqual(expected, day4.count_total_cards_wrapper(data))
#
#
# class Day5(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#             [79, 14, 55, 13],   # seeds
#             [                   # seed -> soil
#                 [50, 98, 2],
#                 [52, 50, 48]
#             ],
#             [                   # soil -> fertilizer
#                 [0, 15, 37],
#                 [37, 52, 2],
#                 [39, 0, 15]
#             ],
#             [                   # fertilizer -> water
#                 [49, 53, 8],
#                 [0, 11, 42],
#                 [42, 0, 7],
#                 [57, 7, 4]
#             ],
#             [                   # water -> light
#                 [88, 18, 7],
#                 [18, 25, 70]
#             ],
#             [                   # light -> temperature
#                 [45, 77, 23],
#                 [81, 45, 19],
#                 [68, 64, 13]
#             ],
#             [                   # temperature -> humidity
#                 [0, 69, 1],
#                 [1, 0, 69]
#             ],
#             [                   # humidity -> location
#                 [60, 56, 37],
#                 [56, 93, 4]
#             ],
#          ], 35),
#         ("day5_a",
#          day5.parse_day5_a(), 806029445)
#     ])
#     def test_find_lowest_location_number(self, _, data, expected):
#         self.assertEqual(expected, day5.find_lowest_location_number(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#             [79, 14, 55, 13],   # seeds
#             [                   # seed -> soil
#                 [50, 98, 2],
#                 [52, 50, 48]
#             ],
#             [                   # soil -> fertilizer
#                 [0, 15, 37],
#                 [37, 52, 2],
#                 [39, 0, 15]
#             ],
#             [                   # fertilizer -> water
#                 [49, 53, 8],
#                 [0, 11, 42],
#                 [42, 0, 7],
#                 [57, 7, 4]
#             ],
#             [                   # water -> light
#                 [88, 18, 7],
#                 [18, 25, 70]
#             ],
#             [                   # light -> temperature
#                 [45, 77, 23],
#                 [81, 45, 19],
#                 [68, 64, 13]
#             ],
#             [                   # temperature -> humidity
#                 [0, 69, 1],
#                 [1, 0, 69]
#             ],
#             [                   # humidity -> location
#                 [60, 56, 37],
#                 [56, 93, 4]
#             ],
#          ], 46),
#         ("day5_b",
#          day5.parse_day5_a(), 59370572)
#     ])
#     def test_find_lowest_location_number_ranges(self, _, data, expected):
#         self.assertEqual(expected, day5.find_lowest_location_number_ranges(data))
#
#     def test_ranges_intersection(self):
#         expected = (45, 55), (), ()
#         a = (30, 60)
#         b = (45, 55)
#         self.assertEqual(expected, day5.ranges_intersection(a, b))
#         expected = (45, 60), (), (60, 97)
#         a = (30, 60)
#         b = (45, 97)
#         self.assertEqual(expected, day5.ranges_intersection(a, b))
#         expected = (), (70, 97), ()
#         a = (30, 60)
#         b = (70, 97)
#         self.assertEqual(expected, day5.ranges_intersection(a, b))
#         expected = (), (10, 27), ()
#         a = (30, 60)
#         b = (10, 27)
#         self.assertEqual(expected, day5.ranges_intersection(a, b))
#         expected = (30, 60), (10, 30), (60, 97)
#         a = (30, 60)
#         b = (10, 97)
#         self.assertEqual(expected, day5.ranges_intersection(a, b))
#
#
# class Day6(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              (7, 15, 30), (9, 40, 200)
#          ], 288),
#         ("day6_a",
#          day6.parse_day6_a(), 1710720)
#     ])
#     def test_calc_num_of_ways_of_beating_the_record(self, _, data, expected):
#         self.assertEqual(expected, day6.calc_num_of_ways_of_beating_the_record(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              (7, 15, 30), (9, 40, 200)
#          ], 71503),
#         # ("day6_b",
#         #  day6.parse_day6_a(), 806029445)
#     ])
#     def test_calc_num_of_ways_of_beating_the_record_v2(self, _, data, expected):
#         self.assertEqual(expected, day6.calc_num_of_ways_of_beating_the_record_v2(data))
#
#
# class Day7(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ("32T3K", 765),
#              ("T55J5", 684),
#              ("KK677", 28),
#              ("KTJJT", 220),
#              ("QQQJA", 483)
#          ], 6440),
#         ("day7_a",
#          day7.parse_day7_a(), 251058093)
#     ])
#     def test_calc_num_of_ways_of_beating_the_record(self, _, data, expected):
#         self.assertEqual(expected, day7.calc_total_winnings(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ("32T3K", 765),
#              ("T55J5", 684),
#              ("KK677", 28),
#              ("KTJJT", 220),
#              ("QQQJA", 483)
#          ], 5905),
#         ("day7_b",
#          day7.parse_day7_a(), 249781879)
#     ])
#     def test_calc_num_of_ways_of_beating_the_record_with_jokers(self, _, data, expected):
#         self.assertEqual(expected, day7.calc_total_winnings_with_jokers(data))
#
#
# class Day8(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#             "RL",
#             ("AAA", "BBB", "CCC"),
#             ("BBB", "DDD", "EEE"),
#             ("CCC", "ZZZ", "GGG"),
#             ("DDD", "DDD", "DDD"),
#             ("EEE", "EEE", "EEE"),
#             ("GGG", "GGG", "GGG"),
#             ("ZZZ", "ZZZ", "ZZZ")
#          ], 2),
#         ("example 2",
#          [
#             "LLR",
#             ("AAA", "BBB", "BBB"),
#             ("BBB", "AAA", "ZZZ"),
#             ("ZZZ", "ZZZ", "ZZZ")
#          ], 6),
#         ("day8_a",
#          day8.parse_day8_a(), 20777)
#     ])
#     def test_calc_num_of_steps(self, _, data, expected):
#         self.assertEqual(expected, day8.calc_num_of_steps(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#             "LR",
#             ("11A", "11B", "XXX"),
#             ("11B", "XXX", "11Z"),
#             ("11Z", "11B", "XXX"),
#             ("22A", "22B", "XXX"),
#             ("22B", "22C", "22C"),
#             ("22C", "22Z", "22Z"),
#             ("22Z", "22B", "22B"),
#             ("XXX", "XXX", "XXX")
#          ], 6),
#
#         ("day8_a",
#          day8.parse_day8_a(), 13289612809129)
#     ])
#     def test_calc_num_of_steps_simultaneous(self, _, data, expected):
#         self.assertEqual(expected, day8.calc_num_of_steps_simultaneous(data))
#
#
# class Day9(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              [0, 3, 6, 9, 12, 15],
#              [1, 3, 6, 10, 15, 21],
#              [10, 13, 16, 21, 30, 45]
#          ], 114),
#         ("day9_a",
#          day9.parse_day9_a(), 1762065988)
#     ])
#     def test_calc_sum_of_extrapolated_values(self, _, data, expected):
#         self.assertEqual(expected, day9.calc_sum_of_extrapolated_values(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              [0, 3, 6, 9, 12, 15],
#              [1, 3, 6, 10, 15, 21],
#              [10, 13, 16, 21, 30, 45]
#          ], 2),
#         ("day9_b",
#          day9.parse_day9_a(), 1066)
#     ])
#     def test_calc_sum_of_extrapolated_values_beginning(self, _, data, expected):
#         self.assertEqual(expected, day9.calc_sum_of_extrapolated_values_beginning(data))
#
#
# class Day10(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#             ".....",
#             ".S-7.",
#             ".|.|.",
#             ".L-J.",
#             "....."
#          ], 4),
#         ("day10_a",
#          day10.parse_day10_a(), 6968)
#     ])
#     def test_calc_num_of_steps(self, _, data, expected):
#         self.assertEqual(expected, day10.calc_num_of_steps(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#             "...........",
#             ".S-------7.",
#             ".|F-----7|.",
#             ".||.....||.",
#             ".||.....||.",
#             ".|L-7.F-J|.",
#             ".|..|.|..|.",
#             ".L--J.L--J.",
#             "..........."
#          ], 4),
#         # ("day10_b",
#         #  day10.parse_day10_a(), 413)
#     ])
#     def test_count_enclosed(self, _, data, expected):
#         self.assertEqual(expected, day10.count_enclosed(data))
#
#
# class Day11(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              "...#......",
#              ".......#..",
#              "#.........",
#              "..........",
#              "......#...",
#              ".#........",
#              ".........#",
#              "..........",
#              ".......#..",
#              "#...#....."
#          ], 374),
#         ("day11_a",
#          day11.parse_day11_a(), 10165598)
#     ])
#     def test_calc_sum_of_lengths(self, _, data, expected):
#         self.assertEqual(expected, day11.calc_sum_of_lengths(data, 2))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              "...#......",
#              ".......#..",
#              "#.........",
#              "..........",
#              "......#...",
#              ".#........",
#              ".........#",
#              "..........",
#              ".......#..",
#              "#...#....."
#          ], 10, 1030),
#         ("example 1",
#          [
#              "...#......",
#              ".......#..",
#              "#.........",
#              "..........",
#              "......#...",
#              ".#........",
#              ".........#",
#              "..........",
#              ".......#..",
#              "#...#....."
#          ], 100, 8410),
#         ("day11_b",
#          day11.parse_day11_a(), 1000000, 678728808158)
#     ])
#     def test_calc_sum_of_lengths_large(self, _, data, factor, expected):
#         self.assertEqual(expected, day11.calc_sum_of_lengths(data, factor))
#
#
# class Day12(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ["???.###", (1, 1, 3)],
#              [".??..??...?##.", (1, 1, 3)],
#              ["?#?#?#?#?#?#?#?", (1, 3, 1, 6)],
#              ["????.#...#...", (4, 1, 1)],
#              ["????.######..#####.", (1, 6, 5)],
#              ["?###????????", (3, 2, 1)]
#          ], 21),
#         ("example 2",
#          [
#              ["???.###", (1, 1, 3)],
#              [".??..??...?##.", (1, 1, 3)],
#              ["?#?#?#?#?#?#?#?", (1, 3, 1, 6)],
#              ["????.#...#...", (4, 1, 1)],
#              ["????.######..#####.", (1, 6, 5)],
#              ["?###????????", (3, 2, 1)],
#              ["??...??...??", (1, 1, 2)],
#              ["???...??...??", (1, 1, 2)]
#          ], 33),
#         ("day12_a",
#          day12.parse_day12_a(), 6871)
#     ])
#     def test_calc_sum_of_possible_arrangements(self, _, data, expected):
#         self.assertEqual(expected, day12.calc_sum_of_possible_arrangements(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ["???.###", (1, 1, 3)],
#              [".??..??...?##.", (1, 1, 3)],
#              ["?#?#?#?#?#?#?#?", (1, 3, 1, 6)],
#              ["????.#...#...", (4, 1, 1)],
#              ["????.######..#####.", (1, 6, 5)],
#              ["?###????????", (3, 2, 1)],
#          ], 525152),
#         ("day12_b",
#          day12.parse_day12_a(), 2043098029844)
#     ])
#     def test_calc_sum_of_possible_arrangements_extended(self, _, data, expected):
#         self.assertEqual(expected, day12.calc_sum_of_possible_arrangements_extended(data))
#
#
# class Day18(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ("R", 6, "70c710"),
#              ("D", 5, "0dc571"),
#              ("L", 2, "5713f0"),
#              ("D", 2, "d2c081"),
#              ("R", 2, "59c680"),
#              ("D", 2, "411b91"),
#              ("L", 5, "8ceee2"),
#              ("U", 2, "caa173"),
#              ("L", 1, "1b58a2"),
#              ("U", 2, "caa171"),
#              ("R", 2, "7807d2"),
#              ("U", 3, "a77fa3"),
#              ("L", 2, "015232"),
#              ("U", 2, "7a21e3")
#          ], 62),
#         ("day18_a",
#          day18.parse_day18_a(), 31171)
#     ])
#     def test_calc_capacity(self, _, data, expected):
#         self.assertEqual(expected, day18.calc_capacity(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ("R", 461937),
#              ("D", 56407),
#              ("R", 356671),
#              ("D", 863240),
#              ("R", 367720),
#              ("D", 266681),
#              ("L", 577262),
#              ("U", 829975),
#              ("L", 112010),
#              ("D", 829975),
#              ("L", 491645),
#              ("U", 686074),
#              ("L", 5411),
#              ("U", 500254)
#          ], 952408144115),
#         ("day18_b",
#          day18.parse_day18_b(), 131431655002266)
#     ])
#     def test_calc_capacity_v2(self, _, data, expected):
#         self.assertEqual(expected, day18.calc_capacity_v2(data))
#
#
# class Day13(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              [
#                  "#.##..##.",
#                  "..#.##.#.",
#                  "##......#",
#                  "##......#",
#                  "..#.##.#.",
#                  "..##..##.",
#                  "#.#.##.#."
#              ],
#
#              [
#                  "#...##..#",
#                  "#....#..#",
#                  "..##..###",
#                  "#####.##.",
#                  "#####.##.",
#                  "..##..###",
#                  "#....#..#"
#              ]
#          ], 405),
#         ("example 2",
#          [
#              [
#                  "...##....",
#                  ".#.##.#..",
#                  ".#....#..",
#                  ".##..##..",
#                  "...##....",
#                  "..####.##",
#                  "#..##..##"
#              ]
#          ], 8),
#         ("day13_a",
#          day13.parse_day13_a(), 35360)
#     ])
#     def test_sum_of_notes(self, _, data, expected):
#         self.assertEqual(expected, day13.sum_of_notes(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              [
#                  "#.##..##.",
#                  "..#.##.#.",
#                  "##......#",
#                  "##......#",
#                  "..#.##.#.",
#                  "..##..##.",
#                  "#.#.##.#."
#              ],
#
#              [
#                  "#...##..#",
#                  "#....#..#",
#                  "..##..###",
#                  "#####.##.",
#                  "#####.##.",
#                  "..##..###",
#                  "#....#..#"
#              ]
#          ], 400),
#
#         ("day13_b",
#          day13.parse_day13_a(), 36755)
#     ])
#     def test_sum_of_notes_v2(self, _, data, expected):
#         self.assertEqual(expected, day13.sum_of_notes_v2(data))
#
#
# class Day14(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ["O", ".", ".", ".", ".", "#", ".", ".", ".", ".", ],
#              ["O", ".", "O", "O", "#", ".", ".", ".", ".", "#", ],
#              [".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ],
#              ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O", ],
#              [".", "O", ".", ".", ".", ".", ".", "O", "#", ".", ],
#              ["O", ".", "#", ".", ".", "O", ".", "#", ".", "#", ],
#              [".", ".", "O", ".", ".", "#", "O", ".", ".", "O", ],
#              [".", ".", ".", ".", ".", ".", ".", "O", ".", ".", ],
#              ["#", ".", ".", ".", ".", "#", "#", "#", ".", ".", ],
#              ["#", "O", "O", ".", ".", "#", ".", ".", ".", ".", ]
#          ], 136),
#         ("day14_a",
#          day14.parse_day14_a(), 109345)
#     ])
#     def test_total_load(self, _, data, expected):
#         self.assertEqual(expected, day14.total_load(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ["O", ".", ".", ".", ".", "#", ".", ".", ".", ".", ],
#              ["O", ".", "O", "O", "#", ".", ".", ".", ".", "#", ],
#              [".", ".", ".", ".", ".", "#", "#", ".", ".", ".", ],
#              ["O", "O", ".", "#", "O", ".", ".", ".", ".", "O", ],
#              [".", "O", ".", ".", ".", ".", ".", "O", "#", ".", ],
#              ["O", ".", "#", ".", ".", "O", ".", "#", ".", "#", ],
#              [".", ".", "O", ".", ".", "#", "O", ".", ".", "O", ],
#              [".", ".", ".", ".", ".", ".", ".", "O", ".", ".", ],
#              ["#", ".", ".", ".", ".", "#", "#", "#", ".", ".", ],
#              ["#", "O", "O", ".", ".", "#", ".", ".", ".", ".", ]
#          ], 64),
#         ("day14_b",
#          day14.parse_day14_a(), 112452)
#     ])
#     def test_total_load_cycles(self, _, data, expected):
#         self.assertEqual(expected, day14.total_load_cycles(data))
#
#
# class Day15(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              "rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9", "ab=5", "pc-", "pc=6", "ot=7"
#          ], 1320),
#         ("day15_a",
#          day15.parse_day15_a(), 518107)
#     ])
#     def test_sum_of_results(self, _, data, expected):
#         self.assertEqual(expected, day15.sum_of_results(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              "rn=1", "cm-", "qp=3", "cm=2", "qp-", "pc=4", "ot=9", "ab=5", "pc-", "pc=6", "ot=7"
#          ], 145),
#         ("day15_b",
#          day15.parse_day15_a(), 303404)
#     ])
#     def test_focusing_power(self, _, data, expected):
#         self.assertEqual(expected, day15.focusing_power(data))
#
#
# class Day16(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              ".|...7....",
#              "|.-.7.....",
#              ".....|-...",
#              "........|.",
#              "..........",
#              ".........7",
#              "..../.77..",
#              ".-.-/..|..",
#              ".|....-|.7",
#              "..//.|...."
#          ], 46),
#         ("day16_a",
#          day16.parse_day16_a(), 7860)
#     ])
#     def test_num_of_energized_tiles(self, _, data, expected):
#         self.assertEqual(expected, day16.num_of_energized_tiles(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              ".|...7....",
#              "|.-.7.....",
#              ".....|-...",
#              "........|.",
#              "..........",
#              ".........7",
#              "..../.77..",
#              ".-.-/..|..",
#              ".|....-|.7",
#              "..//.|...."
#          ], 51),
#         ("day16_b",
#          day16.parse_day16_a(), 8331)
#     ])
#     def test_num_of_energized_tiles_max(self, _, data, expected):
#         self.assertEqual(expected, day16.num_of_energized_tiles_max(data))
#
#
# class Day17(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              list(map(int, list("2413432311323"))),
#              list(map(int, list("3215453535623"))),
#              list(map(int, list("3255245654254"))),
#              list(map(int, list("3446585845452"))),
#              list(map(int, list("4546657867536"))),
#              list(map(int, list("1438598798454"))),
#              list(map(int, list("4457876987766"))),
#              list(map(int, list("3637877979653"))),
#              list(map(int, list("4654967986887"))),
#              list(map(int, list("4564679986453"))),
#              list(map(int, list("1224686865563"))),
#              list(map(int, list("2546548887735"))),
#              list(map(int, list("4322674655533")))
#          ], 0, 3, 102),
#         ("day17_a",
#          day17.parse_day17_a(), 0, 3, 870),
#
#         ("example 2",
#          [
#              list(map(int, list("2413432311323"))),
#              list(map(int, list("3215453535623"))),
#              list(map(int, list("3255245654254"))),
#              list(map(int, list("3446585845452"))),
#              list(map(int, list("4546657867536"))),
#              list(map(int, list("1438598798454"))),
#              list(map(int, list("4457876987766"))),
#              list(map(int, list("3637877979653"))),
#              list(map(int, list("4654967986887"))),
#              list(map(int, list("4564679986453"))),
#              list(map(int, list("1224686865563"))),
#              list(map(int, list("2546548887735"))),
#              list(map(int, list("4322674655533")))
#          ], 4, 10, 94),
#         ("day17_b",
#          day17.parse_day17_a(), 4, 10, 1063)
#     ])
#     def test_least_heat_loss(self, _, data, lower_bound, upper_bound, expected):
#         self.assertEqual(expected, day17.least_heat_loss(data, lower_bound, upper_bound))
#
#
# class Day19(unittest.TestCase):
#     @parameterized.expand([
#         ("example 1",
#          [
#              {
#                  "px": (
#                          ("a<2006", "qkq"),
#                          ("m>2090", "A"),
#                          ("", "rfg")
#                  ),
#                  "pv": (
#                          ("a>1716", "R"),
#                          ("", "A")
#                  ),
#                  "lnx": (
#                          ("m>1548", "A"),
#                          ("", "A")
#                  ),
#                  "rfg": (
#                          ("s<537", "gd"),
#                          ("x>2440", "R"),
#                          ("", "A")
#                  ),
#                  "qs": (
#                          ("s>3448", "A"),
#                          ("", "lnx")
#                  ),
#                  "qkq": (
#                          ("x<1416", "A"),
#                          ("", "crn")
#                  ),
#                  "crn": (
#                          ("x>2662", "A"),
#                          ("", "R")
#                  ),
#                  "in": (
#                          ("s<1351", "px"),
#                          ("", "qqz")
#                  ),
#                  "qqz": (
#                          ("s>2770", "qs"),
#                          ("m<1801", "hdj"),
#                          ("", "R")
#                  ),
#                  "gd": (
#                          ("a>3333", "R"),
#                          ("", "R")
#                  ),
#                  "hdj": (
#                          ("m>838", "A"),
#                          ("", "pv")
#                  )
#              },
#              [
#                 (787, 2655, 1222, 2876),
#                 (1679, 44, 2067, 496),
#                 (2036, 264, 79, 2244),
#                 (2461, 1339, 466, 291),
#                 (2127, 1623, 2188, 1013),
#              ]
#          ], 19114),
#         ("day19_a",
#          day19.parse_day19_a(), 487623)
#     ])
#     def test_sum_of_rating_numbers(self, _, data, expected):
#         self.assertEqual(expected, day19.sum_of_rating_numbers(data))
#
#     @parameterized.expand([
#         ("example 1",
#          [
#              {
#                  "px": (
#                          ("a<2006", "qkq"),
#                          ("m>2090", "A"),
#                          ("", "rfg")
#                  ),
#                  "pv": (
#                          ("a>1716", "R"),
#                          ("", "A")
#                  ),
#                  "lnx": (
#                          ("m>1548", "A"),
#                          ("", "A")
#                  ),
#                  "rfg": (
#                          ("s<537", "gd"),
#                          ("x>2440", "R"),
#                          ("", "A")
#                  ),
#                  "qs": (
#                          ("s>3448", "A"),
#                          ("", "lnx")
#                  ),
#                  "qkq": (
#                          ("x<1416", "A"),
#                          ("", "crn")
#                  ),
#                  "crn": (
#                          ("x>2662", "A"),
#                          ("", "R")
#                  ),
#                  "in": (
#                          ("s<1351", "px"),
#                          ("", "qqz")
#                  ),
#                  "qqz": (
#                          ("s>2770", "qs"),
#                          ("m<1801", "hdj"),
#                          ("", "R")
#                  ),
#                  "gd": (
#                          ("a>3333", "R"),
#                          ("", "R")
#                  ),
#                  "hdj": (
#                          ("m>838", "A"),
#                          ("", "pv")
#                  )
#              },
#              [
#                 (787, 2655, 1222, 2876),
#                 (1679, 44, 2067, 496),
#                 (2036, 264, 79, 2244),
#                 (2461, 1339, 466, 291),
#                 (2127, 1623, 2188, 1013),
#              ]
#          ], 167409079868000),
#         ("day19_b",
#          day19.parse_day19_a(), 113550238315130)
#     ])
#     def test_num_of_valid_ratings(self, _, data, expected):
#         self.assertEqual(expected, day19.num_of_valid_ratings(data))


class Day20(unittest.TestCase):
    @parameterized.expand([
        ("example 1",
         [
             ["a", "b", "c"],
             {
                "a": [["b"]],
                "b": [["c"]],
                "c": [["inv"]]
             },
             {
                 "inv": [["a"], ["c"]]      # 1 - sources
             }
         ], 32000000),
        ("example 2",
         [
             ["a"],
             {
                 "a": [["inv", "con"]],
                 "b": [["con"]],
             },
             {
                 "inv": [["b"], ["a"]],     # 1 - sources
                 "con": [["output"], ["a", "b"]]
             }
         ], 11687500),
        ("day20_a",
         day20.parse_day20_a(), 867118762)
    ])
    def test_pulses_multiplied(self, _, data, expected):
        self.assertEqual(expected, day20.pulses_multiplied(data))

    @parameterized.expand([
        ("day20_b",
         day20.parse_day20_a(), 217317393039529)
    ])
    def test_presses_until_rx(self, _, data, expected):
        self.assertEqual(expected, day20.presses_until_rx(data))
