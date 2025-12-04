import unittest


def parse_grid(input: str) -> list[list[bool]]:
    y: list[list[bool]] = []
    for line in input.strip().splitlines():
        x: list[bool] = []
        for char in line.strip():
            x.append(char == "@")
        y.append(x)
    return y


def occupied(grid: list[list[bool]], x: int, y: int) -> bool:
    try:
        cell = grid[y][x]
    except IndexError:
        return False
    return cell


def solution(grid: list[list[bool]]) -> int:
    total = 0

    print()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # empty cell never counts toward total
            if not cell:
                print(".", end="")
                continue
            # (x-1, y-1) | (x  , y-1) | (x+1, y-1)
            # (x-1, y  ) |            | (x+1, y  )
            # (x-1, y+1) | (x  , y+1) | (x+1, y+1)
            checks = [
                (x - 1, y - 1),
                (x, y - 1),
                (x + 1, y - 1),
                (x - 1, y),
                (x + 1, y),
                (x - 1, y + 1),
                (x, y + 1),
                (x + 1, y + 1),
            ]
            adjacent_free = 0
            for adj_x, adj_y in checks:
                if not occupied(grid, adj_x, adj_y):
                    adjacent_free += 1
            if adjacent_free < 4:
                total += 1
            print(f"{'x' if adjacent_free < 4 else '@'}", end="")
        print()

    return total


class Test(unittest.TestCase):
    example = """
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
""".strip()

    def test_parse_grid(self):
        self.assertEqual(
            parse_grid("..\n@@"),
            [[False, False], [True, True]],
        )

    def test_part1_example(self):
        grid = parse_grid(self.example)
        self.assertEqual(solution(grid), 13)


if __name__ == "__main__":
    unittest.main()
