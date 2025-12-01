import unittest
from typing import List, Tuple


def parse_turn(instruction: str) -> int:
    magnitude = int(instruction[1:])
    if instruction[0] == "L":
        return -magnitude
    else:
        return magnitude


def turn(dial: int, delta: int, size: int = 100) -> Tuple[int, int]:
    """
    Simulates an actual hand turning the dial of a lock left or right.
    """

    zeroes = 0
    left = delta < 0

    for _ in range(0, abs(delta)):
        if left:
            dial -= 1
        else:
            dial += 1

        # dial has wrapped around
        if dial == -1:
            dial = size - 1
        elif dial == size:
            dial = 0

        if dial == 0:
            zeroes += 1

    # dial landing on zero is not a "pass" and gets counted later
    if dial == 0:
        zeroes -= 1

    return dial, zeroes


def solution(input: List[str], dial: int = 50, count_passes: bool = False) -> int:
    zero_counter = 0

    for item in input:
        delta = parse_turn(item)
        dial, zeroes = turn(dial, delta)

        if dial == 0:
            zero_counter += 1
        if count_passes:
            zero_counter += zeroes

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
        self.assertEqual(parse_turn("L1"), -1)
        self.assertEqual(parse_turn("R99"), 99)

    def test_solution_part1_example(self):
        input = self.example_input
        self.assertEqual(solution(input), 3)

    def test_solution_part1_real(self):
        with open("day1_input.txt", "r") as file:
            input = file.readlines()
        self.assertEqual(solution(input), 1089)

    def test_solution_part2_edgecase(self):
        input = [
            "R1000",
            "L1000",
        ]
        self.assertEqual(solution(input, count_passes=True), 20)

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
        self.assertEqual(solution(input, count_passes=True), 8)

    def test_solution_part2_example(self):
        input = self.example_input
        self.assertEqual(solution(input, count_passes=True), 6)

    def test_solution_part2_real(self):
        with open("day1_input.txt", "r") as file:
            input = file.readlines()
        # NOT 6536. This happens if the solution incorrectly accounts observes
        # a passed zero when _starting at 0 and going left_.
        self.assertEqual(solution(input, count_passes=True), 6530)


if __name__ == "__main__":
    unittest.main()
