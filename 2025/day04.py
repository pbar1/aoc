import unittest
from typing import Any, List


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


def count_neighbors(grid: list[list[bool]]) -> list[list[int]]:
    n_y: list[list[int]] = []
    for y, row in enumerate(grid):
        n_x: list[int] = []
        for x, _ in enumerate(row):
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
            neighbors = 0
            for adj_x, adj_y in checks:
                print(occupied(grid, adj_x, adj_y), adj_x, adj_y)
                if occupied(grid, adj_x, adj_y):
                    neighbors += 1
            break
            n_x.append(neighbors)
        n_y.append(n_x)
    return n_y


def print_grid(a: List[List[Any]]):
    width = max(len(str(int(x))) for row in a for x in row)
    for row in a:
        print(" ".join(f"{x:{width}}" for x in row))


def solution(grid: list[list[bool]]) -> int:
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
            # if y == 0 and x == 3:
            #     print(adjacent_occupied)
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

    def test_part1_real(self):
        with open("inputs/day04.txt", "r") as file:
            input = file.read().strip()
        grid = parse_grid(input)
        self.assertEqual(solution(grid), 1363)


if __name__ == "__main__":
    unittest.main()
