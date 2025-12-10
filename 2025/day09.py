import unittest


def parse_input(input: str) -> list[tuple[int, int]]:
    points: list[tuple[int, int]] = []
    for line in input.strip().splitlines():
        [x, y] = line.split(",")
        points.append((int(x), int(y)))
    return points


def solve_part1(input: list[tuple[int, int]]) -> int:
    max_area = -1

    for a_x, a_y in input:
        for b_x, b_y in input:
            if a_x == b_x or a_y == b_y:
                continue
            x = abs(a_x - b_x) + 1
            y = abs(a_y - b_y) + 1
            max_area = max(x * y, max_area)

    return max_area


def solve_part2(input: list[tuple[int, int]]) -> int:
    return -1


class Test(unittest.TestCase):
    example = """
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
""".strip()

    def test_part1_example(self):
        input = parse_input(self.example)
        self.assertEqual(solve_part1(input), 50)

    def test_part1_real(self):
        with open("inputs/day09.txt", "r") as file:
            input = parse_input(file.read().strip())
        self.assertEqual(solve_part1(input), -1)

    def test_part2_example(self):
        input = parse_input(self.example)
        self.assertEqual(solve_part2(input), -1)

    def test_part2_real(self):
        with open("inputs/day09.txt", "r") as file:
            input = parse_input(file.read().strip())
        self.assertEqual(solve_part2(input), -1)


if __name__ == "__main__":
    unittest.main()
