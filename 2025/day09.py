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
    max_x = -1
    max_y = -1

    for x, y in input:
        max_x = max(x, max_x)
        max_y = max(y, max_y)

    boundary: set[tuple[int, int]] = set()
    for i in range(0, len(input)):
        if i == len(input) - 1:
            j = 0
        else:
            j = i + 1
        cur_x, cur_y = input[i]
        nxt_x, nxt_y = input[j]

        # same x-axis, move vertically
        if cur_x == nxt_x:
            lo_y = min(cur_y, nxt_y)
            hi_y = max(cur_y, nxt_y)
            for y in range(lo_y, hi_y + 1):
                boundary.add((cur_x, y))

        # same y-axis, move horizontally
        if cur_y == nxt_y:
            lo_x = min(cur_x, nxt_x)
            hi_x = max(cur_x, nxt_x)
            for x in range(lo_x, hi_x + 1):
                boundary.add((x, cur_y))

    print(f"boundary points: {len(boundary)}")

    # scan across each row for min, max x
    minmax_xs: dict[int, tuple[int, int]] = dict()
    for y in range(0, max_y + 1):
        lo_x = -1
        hi_x = -1
        for x in range(0, max_x + 1):
            if (x, y) in boundary:
                if lo_x == -1:
                    lo_x = x
                hi_x = x
        minmax_xs[y] = (lo_x, hi_x)

    # print(minmax_xs)

    # scan across each col for min, max y
    minmax_ys: dict[int, tuple[int, int]] = dict()
    for x in range(0, max_x + 1):
        lo_y = -1
        hi_y = -1
        for y in range(0, max_y + 1):
            if (x, y) in boundary:
                if lo_y == -1:
                    lo_y = y
                hi_y = y
        minmax_ys[x] = (lo_y, hi_y)

    # print(minmax_ys)

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
        self.assertEqual(solve_part1(input), 4781377701)

    def test_part2_example(self):
        input = parse_input(self.example)
        self.assertEqual(solve_part2(input), -1)

    def test_part2_real(self):
        with open("inputs/day09.txt", "r") as file:
            input = parse_input(file.read().strip())
        self.assertEqual(solve_part2(input), -1)


if __name__ == "__main__":
    unittest.main()
