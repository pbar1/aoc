import unittest
from typing import List, Tuple


def parse_product_ids(input: str) -> List[Tuple[str, str]]:
    product_ids: List[Tuple[str, str]] = []
    for parsed in input.split(","):
        [first, second] = parsed.split("-")
        product_ids.append((first, second))
    return product_ids


def solution(input: List[Tuple[str, str]]) -> int:
    pass


class Test(unittest.TestCase):
    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    def test_parse_product_ids(self):
        input = "11-22,95-115"
        self.assertEqual(
            parse_product_ids(input),
            [
                ("11", "22"),
                ("95", "115"),
            ],
        )

    def test_part1_example(self):
        input = parse_product_ids(self.example_input)
        self.assertEqual(solution(input), 1227775554)


if __name__ == "__main__":
    unittest.main()
