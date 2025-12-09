import unittest
from dataclasses import dataclass
from typing import Optional, Tuple


@dataclass(order=True, frozen=True)
class Point:
    x: int
    y: int
    z: int


def parse_input(input: str) -> list[Point]:
    points: list[Point] = []
    for line in input.splitlines():
        [x, y, z] = line.split(",")
        points.append(Point(int(x), int(y), int(z)))
    return points


def distance(a: Point, b: Point) -> float:
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2 + (a.z - b.z) ** 2) ** 0.5


def solve(points: list[Point]) -> int:
    friends: dict[Point, Tuple[Point, float]] = {}

    for a in points:
        shortest: Optional[float] = None
        for b in points:
            if a == b:
                continue
            d = distance(a, b)
            if not shortest or d < shortest:
                shortest = d
                friends[a] = (b, d)

    friend_list: list[Tuple[float, Point, Point]] = []
    for a, (b, d) in friends.items():
        friend_list.append((d, a, b))
    friend_list.sort()

    sets: list[set[Point]] = []
    for _, a, b in friend_list:
        added = False
        for s in sets:
            if a in s or b in s:
                s.add(a)
                s.add(b)
                added = True
                break
        if not added:
            sets.append({a, b})

    sets.sort(key=lambda x: len(x), reverse=True)

    for s in sets:
        print(len(s), s)

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

    def test_distance(self):
        a = Point(162, 817, 812)
        b = Point(425, 690, 689)
        self.assertAlmostEqual(distance(a, b), 316.90219311327)

    def test_part1_example(self):
        points = parse_input(self.example)
        self.assertEqual(solve(points), 40)

    # def test_part1_real(self):
    #     with open("inputs/day08.txt", "r") as file:
    #         points = parse_input(file.read().strip())
    #     self.assertEqual(solve(points), -1)


if __name__ == "__main__":
    unittest.main()
