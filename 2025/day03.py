import unittest
from typing import List


def max_joltage(bank: str, digits: int) -> int:
    joltage = ""

    start = 0
    while digits > 0:
        end = len(bank) - digits + 1

        # useless but safe comparison for the first iteration
        max_i, max_digit = start, bank[start]
        for i in range(start, end):
            digit = bank[i]
            if digit > max_digit:
                max_i, max_digit = i, digit

        joltage += max_digit
        start = max_i + 1
        digits -= 1  # drain digit count

    return int(joltage)


def solution(banks: List[str], digits: int) -> int:
    sum = 0
    for bank in banks:
        sum += max_joltage(bank, digits)
    return sum


class Test(unittest.TestCase):
    example_input = """
987654321111111
811111111111119
234234234234278
818181911112111
"""

    def test_part1_example(self):
        input = self.example_input.strip().splitlines()
        self.assertEqual(solution(input, 2), 357)

    def test_part1_real(self):
        with open("inputs/day03.txt", "r") as file:
            input = [line.strip() for line in file.readlines()]
        self.assertEqual(solution(input, 2), 17405)

    def test_part2_example(self):
        input = self.example_input.strip().splitlines()
        self.assertEqual(solution(input, 12), 3121910778619)

    def test_part2_real(self):
        with open("inputs/day03.txt", "r") as file:
            input = [line.strip() for line in file.readlines()]
        self.assertEqual(solution(input, 12), 171990312704598)


if __name__ == "__main__":
    unittest.main()
