import unittest


def dbg(input: int, size: int, char: str = "|") -> str:
    return f"{input:>0{size}b}".replace("0", ".").replace("1", char)


def bitfield(n: int, size: int) -> list[int]:
    return [int(c) for c in f"{n:>0{size}b}"]


def solve(input: str, count_paths: bool = False) -> int:
    input = input.replace(".", "0")
    input = input.replace("^", "1")
    input = input.replace("S", "1")

    lines = input.splitlines()

    beam = int(lines.pop(0), 2)
    width = len(lines[0])

    splits = 0
    position_hits = [0] * width

    for line in lines:
        # splitters act as XOR on the beam index
        splitter_mask = int(line, 2)

        # find the active splitters and count only them
        splitter_mask &= beam
        splits += splitter_mask.bit_count()

        # find positions of the new paths of the beam
        new_left = splitter_mask << 1
        new_right = splitter_mask >> 1

        # accumulate unique hits into a position by counting its hits for both
        # left and right splits
        for i, bit in enumerate(bitfield(new_left, width)):
            position_hits[i] += bit
        for i, bit in enumerate(bitfield(new_right, width)):
            position_hits[i] += bit

        # beams act as OR with other beams
        or_mask = new_left | new_right

        # turn off only split beams with NAND, and apply the splits with OR
        beam &= ~splitter_mask
        beam |= or_mask

        # print(f"split: {dbg(splitter_mask, width, "^")}  ", end="")
        # print(f" beams: {dbg(or_mask, width)}  ", end="")
        # print(f" final: {dbg(beam, width)}  ", end="")
        # print()

    if count_paths:
        return sum(position_hits)
    return splits


class Test(unittest.TestCase):
    example = """
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
""".strip()

    def test_part1_example(self):
        input = self.example
        self.assertEqual(solve(input), 21)

    def test_part1_real(self):
        with open("inputs/day07.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(solve(input), 1678)

    def test_part2_example(self):
        input = self.example
        self.assertEqual(solve(input, count_paths=True), 40)

    def test_part2_real(self):
        with open("inputs/day07.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(solve(input, count_paths=True), -1)  # 3354 is too low


if __name__ == "__main__":
    unittest.main()
