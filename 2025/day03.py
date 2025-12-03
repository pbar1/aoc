import unittest
from typing import List, Optional, Tuple


def max_battery(bank: str) -> int:
    top1: Optional[Tuple[int, str]] = None

    for i, val in enumerate(bank):
        if top1 is None:
            top1 = (i, val)
            continue
        if val > top1[1]:
            top1 = (i, val)

    if not top1:
        raise Exception("unable to find top1")

    # if top1 is all the way to the right, then top2 must be on the left
    # otherwise just do max again starting after top1
    reverse = False
    if top1[0] == len(bank) - 1:
        reverse = True
        subbank = bank[: top1[0]]
    else:
        subbank = bank[top1[0] + 1 :]

    top2: Optional[Tuple[int, str]] = None

    for i, val in enumerate(subbank):
        if top2 is None:
            top2 = (i, val)
            continue
        if val > top2[1]:
            top2 = (i, val)

    if not top2:
        raise Exception("unable to find top2")

    if reverse:
        return int(top2[1] + top1[1])
    return int(top1[1] + top2[1])


def part1(banks: List[str]) -> int:
    sum = 0

    for bank in banks:
        battery = max_battery(bank)
        sum += battery

    return sum


class Test(unittest.TestCase):
    example_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

    def test_max_battery(self):
        self.assertEqual(max_battery("987654321111111"), 98)
        self.assertEqual(max_battery("811111111111119"), 89)
        self.assertEqual(
            max_battery(
                "1687783252471642886241864885417574245161768635576844528554852355566876467348472654541656343253424539"
            ),
            89,
        )

    def test_part1_example(self):
        input = self.example_input.strip().splitlines()
        self.assertEqual(part1(input), 357)

    def test_part1_real(self):
        with open("inputs/day03.txt", "r") as file:
            input = [line.strip() for line in file.readlines()]
        self.assertEqual(part1(input), 17405)


if __name__ == "__main__":
    unittest.main()
