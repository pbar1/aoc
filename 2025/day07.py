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
    # For part 2: track the number of paths at each position
    paths = [0] * width
    # Initialize starting position with 1 path
    for i, bit in enumerate(bitfield(beam, width)):
        if bit:
            paths[i] = 1

    for line in lines:
        # splitters act as XOR on the beam index
        splitter_mask = int(line, 2)

        # find the active splitters and count only them
        splitter_mask &= beam
        splits += splitter_mask.bit_count()

        # find positions of the new paths of the beam
        split_left = splitter_mask << 1
        split_right = splitter_mask >> 1

        # turn off only split beams with NAND
        unsplit = beam & ~splitter_mask
        # combine all valid beams with OR
        beam = unsplit | split_left | split_right

        if count_paths:
            new_paths = [0] * width

            for i, bit in enumerate(bitfield(unsplit, width)):
                if bit:
                    new_paths[i] += paths[i]

            for i, bit in enumerate(bitfield(split_left, width)):
                if bit:
                    new_paths[i] += paths[i + 1]

            for i, bit in enumerate(bitfield(split_right, width)):
                if bit:
                    new_paths[i] += paths[i - 1]

            paths = new_paths

        # print(f"split: {dbg(splitter_mask, width, "^")}  ", end="")
        # print(f"beams: {dbg(or_mask, width)}  ", end="")
        # print(f"unsplit: {dbg(unsplit, width)}  ", end="")
        # print(f"final: {dbg(beam, width)}  ", end="")

    if count_paths:
        return sum(paths)
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
        self.assertEqual(solve(input, count_paths=True), 357525737893560)


if __name__ == "__main__":
    unittest.main()
