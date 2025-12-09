import unittest
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int
    z: int


def parse_input(input: str) -> list[Point]:
    points: list[Point] = []
    for line in input.splitlines():
        print(line)
        [x, y, z] = line.split(",")
        points.append(Point(int(x), int(y), int(z)))
    return points


def solve(points: list[Point]) -> int:
    return -1


class Test(unittest.TestCase):
    example = """
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
""".strip()

    def test_part1_example(self):
        points = parse_input(self.example)
        self.assertEqual(solve(points), -1)

    def test_part1_real(self):
        with open("inputs/day08.txt", "r") as file:
            points = parse_input(file.read().strip())
        self.assertEqual(solve(points), -1)


if __name__ == "__main__":
    unittest.main()
