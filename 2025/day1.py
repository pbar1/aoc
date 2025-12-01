import unittest
from typing import List, Tuple


def parse_rotation(rotation: str) -> Tuple[bool, int]:
    direction = rotation[:1] == "L"
    magnitude = int(rotation[1:])
    return (direction, magnitude)


def add_mod(x: int, y: int, size: int = 100) -> int:
    return (x + y) % size


def sub_mod(x: int, y: int, size: int = 100) -> int:
    return (x - y) % size


def solution(input: List[str], dial: int = 50) -> int:
    zero_counter = 0

    for item in input:
        left, magnitude = parse_rotation(item)

        if left:
            dial = sub_mod(dial, magnitude)
        else:
            dial = add_mod(dial, magnitude)

        if dial == 0:
            zero_counter += 1

    return zero_counter


class Test(unittest.TestCase):

    def test_parse_rotation(self):
        self.assertEqual(parse_rotation("L1"), (True, 1))
        self.assertEqual(parse_rotation("R99"), (False, 99))

    def test_solution_example(self):
        input = [
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
        self.assertEqual(solution(input), 3)

    def test_solution_real(self):
        with open("day1_input.txt", "r+") as file:
            input = file.readlines()
        self.assertEqual(solution(input), 1089)


if __name__ == "__main__":
    unittest.main()
