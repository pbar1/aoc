import unittest


def dbg(input: int, size: int, char: str = "|") -> str:
    return f"{input:>0{size}b}".replace("0", ".").replace("1", char)


def part1(input: str) -> int:
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

        # beams act as OR with other beams
        or_mask = new_left | new_right

        # turn off only split beams with NAND, and apply the splits with OR
        beam &= ~splitter_mask
        beam |= or_mask

        print(f"split: {dbg(splitter_mask, width, "^")}  ", end="")
        print(f" beams: {dbg(or_mask, width)}  ", end="")
        print(f" final: {dbg(beam, width)}  ", end="")
        print()

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
        self.assertEqual(part1(input), 21)

    # def test_part1_real(self):
    #     with open("inputs/day07.txt", "r") as file:
    #         input = file.read().strip()
    #     self.assertEqual(part1(input), 1678)


if __name__ == "__main__":
    unittest.main()
