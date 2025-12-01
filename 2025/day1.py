import unittest
from typing import List, Tuple


def parse_rotation(rotation: str) -> Tuple[bool, int]:
    direction = rotation[:1] == "L"
    magnitude = int(rotation[1:])
    return (direction, magnitude)


def turn(dial: int, left: bool, magnitude: int, size: int = 100) -> Tuple[int, int]:
    passed_zero = 0

    for _ in range(0, magnitude):
        if left:
            dial -= 1
        else:
            dial += 1

        if dial == -1:
            dial = size - 1
        elif dial == size:
            dial = 0

        if dial == 0:
            passed_zero += 1

    # dial landing on zero is not a "pass" and gets counted later
    if dial == 0:
        passed_zero -= 1

    return (dial, passed_zero)


def solution(input: List[str], dial: int = 50, count_clicks: bool = False) -> int:
    zero_counter = 0

    for item in input:
        left, magnitude = parse_rotation(item)
        dial, passed_zero = turn(dial, left, magnitude)

        if dial == 0:
            zero_counter += 1
        if count_clicks:
            zero_counter += passed_zero

    return zero_counter


class Test(unittest.TestCase):
    example_input = [
        "L68",
        "L30",
        "R48",
        "L5",
        "R60",
        "L55",
        "L1",
        "L99",
        "R14",
        "L82",
    ]

    def test_parse_rotation(self):
        self.assertEqual(parse_rotation("L1"), (True, 1))
        self.assertEqual(parse_rotation("R99"), (False, 99))

    def test_solution_part1_example(self):
        input = self.example_input
        self.assertEqual(solution(input), 3)

    def test_solution_part1_real(self):
        with open("day1_input.txt", "r+") as file:
            input = file.readlines()
        self.assertEqual(solution(input), 1089)

    def test_solution_part2_edgecase(self):
        input = [
            "R1000",
            "L1000",
        ]
        self.assertEqual(solution(input, count_clicks=True), 20)

    def test_solution_part2_custom(self):
        input = [
            "L51",  # 50 - 51 -> 99, zeroes = 1
            "R1",  # 99 + 1 -> 0, zeroes = 2
            "L100",  # 0 - 100 -> 0, zeroes = 3
            "R100",  # 0 + 100 -> 0, zeroes = 4
            "R200",  # 0 + 200 -> 0, zeroes = 6
            "R1",  # 0 + 1 -> 1, zeroes = 6
            "L101",  # 1 - 101 -> 0, zeroes = 8
        ]
        self.assertEqual(solution(input, count_clicks=True), 8)

    def test_solution_part2_example(self):
        input = self.example_input
        self.assertEqual(solution(input, count_clicks=True), 6)

    def test_solution_part2_real(self):
        with open("day1_input.txt", "r+") as file:
            input = file.readlines()
        self.assertEqual(solution(input, count_clicks=True), 6530)  # not 6536


if __name__ == "__main__":
    unittest.main()
