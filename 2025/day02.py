import unittest
from functools import cache
from math import isqrt
from typing import Generator, List, Set, Tuple


def parse_id_ranges(input: str) -> List[Tuple[str, str]]:
    id_range: List[Tuple[str, str]] = []
    for parsed in input.split(","):
        [first, last] = parsed.split("-")
        id_range.append((first, last))
    return id_range


@cache
def factors_without_n(n: int) -> Set[int]:
    divisors: Set[int] = set()
    if n == 1:
        return divisors
    for i in range(1, isqrt(n) + 1):
        if n % i == 0:
            divisors.add(i)
            j = n // i
            if j != i and j != n:
                divisors.add(j)
    return divisors


def chunkstr(s: str, size: int) -> Generator[str, None, None]:
    for i in range(0, len(s), size):
        yield s[i : i + size]


def solution_part1(input: List[Tuple[str, str]]) -> int:
    total = 0

    for first, last in input:
        for id in range(int(first), int(last) + 1):
            s = str(id)
            if s[: len(s) // 2] == s[len(s) // 2 :]:
                total += id

    return total


def solution_part2(input: List[Tuple[str, str]]) -> int:
    total = 0

    for first, last in input:
        for id in range(int(first), int(last) + 1):
            s = str(id)
            divisors = factors_without_n(len(s))
            for divisor in divisors:
                chunks = set(chunkstr(s, divisor))
                if len(chunks) == 1:
                    total += id
                    break

    return total


class Test(unittest.TestCase):
    example_input = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    def test_parse_id_ranges(self):
        input = "11-22,95-115"
        self.assertEqual(
            parse_id_ranges(input),
            [("11", "22"), ("95", "115")],
        )

    def test_factors(self):
        self.assertEqual(factors_without_n(1), set())
        self.assertEqual(factors_without_n(2), {1})
        self.assertEqual(factors_without_n(3), {1})
        self.assertEqual(factors_without_n(10), {1, 2, 5})

    def test_chunkstr(self):
        self.assertEqual(list(chunkstr("101", 1)), ["1", "0", "1"])
        self.assertEqual(list(chunkstr("012345", 1)), ["0", "1", "2", "3", "4", "5"])
        self.assertEqual(list(chunkstr("012345", 2)), ["01", "23", "45"])
        self.assertEqual(list(chunkstr("012345", 3)), ["012", "345"])
        self.assertEqual(list(chunkstr("012345", 6)), ["012345"])

    def test_part1_example(self):
        input = parse_id_ranges(self.example_input)
        self.assertEqual(solution_part1(input), 1227775554)

    def test_part1_real(self):
        with open("inputs/day02.txt", "r") as file:
            real_input = file.read()
        input = parse_id_ranges(real_input)
        self.assertEqual(solution_part1(input), 18893502033)

    def test_part2_example(self):
        input = parse_id_ranges(self.example_input)
        self.assertEqual(solution_part2(input), 4174379265)

    def test_part2_real(self):
        with open("inputs/day02.txt", "r") as file:
            real_input = file.read()
        input = parse_id_ranges(real_input)
        self.assertEqual(solution_part2(input), 26202168557)


if __name__ == "__main__":
    unittest.main()
