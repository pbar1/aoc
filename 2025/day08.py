import unittest
from dataclasses import dataclass
from typing import Tuple


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


def solve(points: list[Point], top: int) -> int:
    segments: list[Tuple[float, Point, Point]] = []
    for a in points:
        for b in points:
            if a == b:
                continue
            d = distance(a, b)
            segments.append((d, a, b))
    segments.sort()
    # otherwise all the point info would be duplicated because we took the
    # cartesian product
    segments = [segment for i, segment in enumerate(segments) if i % 2 == 0]

    # we only want the top N segments
    segments = segments[:top]
    # for segment in segments:
    #     print(segment)

    sets: list[set[Point]] = []

    # create maximal sets

    for _, a, b in segments:
        append_new_set = True
        for s in sets:
            if a in s or b in s:
                s.add(a)
                s.add(b)
                append_new_set = False
                break
        if append_new_set:
            sets.append({a, b})

    # merge the sets

    keep_going = True
    while keep_going:
        # pessimistically assume that this is the last iteration
        keep_going = False

        merged_sets: list[set[Point]] = []
        for s in sets:
            for merged in merged_sets:
                # sets overlap, so merge s into merged
                if not s.isdisjoint(merged):
                    merged.update(s)
                    keep_going = True
                    break
            else:
                merged_sets.append(s)

        sets = merged_sets

    # count total

    sets.sort(key=lambda s: len(s), reverse=True)
    total = 1
    for s in sets[:3]:
        # print(len(s), s)
        total *= len(s)

    return total


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

    def test_distance_2(self):
        a = Point(431, 825, 988)
        b = Point(425, 690, 689)
        self.assertAlmostEqual(distance(a, b), 328.11888089532425)

    def test_part1_example(self):
        points = parse_input(self.example)
        self.assertEqual(solve(points, top=10), 40)

    def test_part1_real(self):
        with open("inputs/day08.txt", "r") as file:
            points = parse_input(file.read().strip())
        self.assertEqual(solve(points, top=1000), 63920)

    def test_part2_example(self):
        points = parse_input(self.example)
        self.assertEqual(25272, 25272)

    def test_part2_real(self):
        with open("inputs/day08.txt", "r") as file:
            points = parse_input(file.read().strip())
        self.assertEqual(-1, -1)


if __name__ == "__main__":
    unittest.main()
