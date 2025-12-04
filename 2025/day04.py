import unittest


def parse_grid(input: str) -> list[list[bool]]:
    y: list[list[bool]] = []
    for line in input.strip().splitlines():
        x: list[bool] = []
        for char in line.strip():
            x.append(char == "@")
        y.append(x)
    return y


def solution(input: list[list[str]]) -> int:
    return -1


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

    # def test_part1_example(self):
    #     self.assertEqual(solution())


if __name__ == "__main__":
    unittest.main()
