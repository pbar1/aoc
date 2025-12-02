import unittest
from typing import List, Set, Tuple


def parse_id_ranges(input: str) -> List[Tuple[str, str]]:
    id_range: List[Tuple[str, str]] = []
    for parsed in input.split(","):
        [first, last] = parsed.split("-")
        id_range.append((first, last))
    return id_range


def solution(input: List[Tuple[str, str]]) -> int:
    total = 0

    for first, last in input:
        for id in range(int(first), int(last) + 1):
            s = str(id)
            a, b = s[: len(s) // 2], s[len(s) // 2 :]
            if a == b:
                total += id

    return total


class Test(unittest.TestCase):
    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    def test_parse_id_ranges(self):
        input = "11-22,95-115"
        self.assertEqual(
            parse_id_ranges(input),
            [
                ("11", "22"),
                ("95", "115"),
            ],
        )

    def test_part1_example(self):
        input = parse_id_ranges(self.example_input)
        self.assertEqual(solution(input), 1227775554)

    def test_part1_real(self):
        with open("inputs/day02.txt", "r") as file:
            real_input = file.read()
        input = parse_id_ranges(real_input)
        self.assertEqual(solution(input), 18893502033)


if __name__ == "__main__":
    unittest.main()
