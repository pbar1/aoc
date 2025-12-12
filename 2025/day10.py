import unittest


def solve_part1(input: str) -> int:
    return -1


def solve_part2(input: str) -> int:
    return -1


class Test(unittest.TestCase):
    example = """
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
""".strip()

    def test_part1_example(self):
        input = self.example
        self.assertEqual(solve_part1(input), 7)

    def test_part1_real(self):
        with open("inputs/day09.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(solve_part1(input), -1)

    def test_part2_example(self):
        input = self.example
        self.assertEqual(solve_part2(input), -1)

    def test_part2_real(self):
        with open("inputs/day09.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(solve_part2(input), -1)


if __name__ == "__main__":
    unittest.main()
