import unittest
from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class Ingredients:
    fresh_id_ranges: List[Tuple[int, int]]
    available_ids: List[int]


def parse_input(input: str) -> Ingredients:
    [ranges, available] = input.split("\n\n")

    fresh_id_ranges: List[Tuple[int, int]] = []
    for range in ranges.strip().splitlines():
        [start, end] = range.strip().split("-")
        fresh_id_ranges.append((int(start), int(end)))

    available_ids = [int(item.strip()) for item in available.strip().splitlines()]

    return Ingredients(fresh_id_ranges, available_ids)


def solution(ingredients: Ingredients) -> int:
    fresh_total = 0

    for candidate in ingredients.available_ids:
        for start, end in ingredients.fresh_id_ranges:
            if start <= candidate <= end:
                fresh_total += 1
                break

    return fresh_total


class Test(unittest.TestCase):
    example = """
3-5
10-14
16-20
12-18

1
5
8
11
17
32
""".strip()

    def test_parse_input(self):
        self.assertEqual(
            parse_input(self.example),
            Ingredients([(3, 5), (10, 14), (16, 20), (12, 18)], [1, 5, 8, 11, 17, 32]),
        )

    def test_part1_example(self):
        ingredients = parse_input(self.example)
        self.assertEqual(solution(ingredients), 3)

    def test_part1_real(self):
        with open("inputs/day05.txt") as file:
            ingredients = parse_input(file.read().strip())
        self.assertEqual(solution(ingredients), -1)


if __name__ == "__main__":
    unittest.main()
