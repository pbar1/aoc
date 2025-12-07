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

    total_splits = 0
    total_paths = bitfield(beam, width)

    for line in lines:
        splitters = int(line, 2)

        # find the active splitters and count only them
        splitters &= beam
        total_splits += splitters.bit_count()

        # find positions of the new paths of the beam
        split_left = splitters << 1
        split_right = splitters >> 1

        # turn off only split beams with NAND
        unsplit = beam & ~splitters
        # combine all valid beams with OR
        beam = unsplit | split_left | split_right

        if count_paths:
            new_paths = [0] * width
            u = bitfield(unsplit, width)
            l = bitfield(split_left, width)
            r = bitfield(split_right, width)

            # since we're tracing paths, we need to grab the previous count
            # from the proper location prior to shift. for unsplit there is no
            # offset, but for left and right, they are (counterintuitively) +1
            # and -1, since that is the offset needed to "undo" the shift
            for i in range(0, width):
                if u[i]:
                    new_paths[i] += total_paths[i]
                if l[i]:
                    new_paths[i] += total_paths[i + 1]
                if r[i]:
                    new_paths[i] += total_paths[i - 1]

            total_paths = new_paths

        # print(f"split: {dbg(splitter_mask, width, "^")}  ", end="")
        # print(f"beams: {dbg(or_mask, width)}  ", end="")
        # print(f"unsplit: {dbg(unsplit, width)}  ", end="")
        # print(f"final: {dbg(beam, width)}  ", end="")

    if count_paths:
        return sum(total_paths)
    return total_splits


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
