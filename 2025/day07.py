import re
import unittest


def dbg(input: int, char: str = "|", size: int = 15) -> str:
    return f"{input:>0{size}b}".replace("0", ".").replace("1", char)


def part1(input: str) -> int:
    input = input.replace(".", "0")
    input = input.replace("^", "1")
    input = input.replace("S", "1")

    lines = input.splitlines()
    start = lines.pop(0)

    # print(start)
    # print()

    beam_bits = int(start, 2)

    splits = 0

    for line in lines:
        # splitters act as XOR on the beam index
        splitter_mask = int(line, 2)

        # find positions of the new paths of the beam
        new_beams: list[int] = []
        for match in re.finditer("1", line):
            new_beams.append(match.start() - 1)
            new_beams.append(match.start() + 1)
        beam_line = list("0" * len(line))
        for i in new_beams:
            beam_line[i] = "1"

        # beams act as OR with other beams
        or_mask = int("".join(beam_line), 2)

        # simulate what would happen if the splitter was always applied, ie
        # with XOR, and save it for later without mutating the input
        unused = beam_bits ^ splitter_mask
        unused |= or_mask

        # apply the actual logic by turing off incoming beams with AND-NOT,
        # which is slightly different from XOR by being path-dependent instead
        # of commutative
        beam_bits &= ~splitter_mask
        beam_bits |= or_mask

        # find the difference between the XOR and AND-NOT results, which are
        # the unused splitters
        unused ^= beam_bits

        # count the total splitters - unused splitters
        splits += splitter_mask.bit_count() - unused.bit_count()

        # print(
        #     f"split: {dbg(splitter_mask, "^")}  beams: {dbg(or_mask)}  final: {dbg(beam_bits)}  unused: {dbg(unused)}"
        # )

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

    def test_part1_real(self):
        with open("inputs/day07.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(part1(input), 1678)


if __name__ == "__main__":
    unittest.main()
