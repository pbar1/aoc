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
    if x < 0 or y < 0 or x >= len(grid[0]) or y >= len(grid):
        return False
    return grid[y][x]


def accessible_rolls(grid: list[list[bool]]) -> int:
    total = 0

    print()
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            # empty cell never counts toward total
            if not cell:
                print(".", end="")
                continue

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
            adjacent_occupied = 0
            for adj_x, adj_y in checks:
                if occupied(grid, adj_x, adj_y):
                    adjacent_occupied += 1
            if adjacent_occupied < 4:
                total += 1
            print(f"{'x' if adjacent_occupied < 4 else '@'}", end="")
        print()

    return total


def removable_rolls(grid: list[list[bool]], keep_going: bool) -> int:
    total = 0

    while True:
        removed_queue = 0
        print()
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                # empty cell never counts toward total
                if not cell:
                    print(".", end="")
                    continue

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
                adjacent_occupied = 0
                for adj_x, adj_y in checks:
                    if occupied(grid, adj_x, adj_y):
                        adjacent_occupied += 1
                if adjacent_occupied < 4:
                    # remove the roll
                    grid[y][x] = False
                    removed_queue += 1
                print(f"{'x' if adjacent_occupied < 4 else '@'}", end="")
            print()
        if removed_queue == 0 or not keep_going:
            break
        total += removed_queue

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
        self.assertEqual(accessible_rolls(grid), 13)

    def test_part1_real(self):
        with open("inputs/day04.txt", "r") as file:
            input = file.read().strip()
        grid = parse_grid(input)
        self.assertEqual(accessible_rolls(grid), 1363)

    def test_part2_example(self):
        grid = parse_grid(self.example)
        self.assertEqual(removable_rolls(grid, keep_going=True), 43)

    # def test_part2_real(self):
    #     with open("inputs/day04.txt", "r") as file:
    #         input = file.read().strip()
    #     grid = parse_grid(input)
    #     self.assertEqual(removable_rolls(grid), -1)


if __name__ == "__main__":
    unittest.main()
