import re
import unittest


def product(xs: list[int]) -> int:
    p = 1
    for x in xs:
        p *= x
    return p


def part1(input: str) -> int:
    lines = input.splitlines()

    # get all the operations as an array
    ops = list(map(lambda op: op.strip(), lines.pop().strip().split()))

    # set all slots to the identity value for each operation
    slots = list(map(lambda x: 0 if x == "+" else 1, ops))

    for line in lines:
        for i, num in enumerate(line.split()):
            num = int(num.strip())
            if ops[i] == "+":
                slots[i] += num
            else:
                slots[i] *= num

    return sum(slots)


def part2(input: str) -> int:
    lines = input.splitlines()
    last = lines.pop()
    rows = len(lines)

    ops = list(map(lambda op: op.strip(), last.split()))

    widths = list(map(lambda w: len(w), re.split(r"[+*]{1}", last)))
    widths.pop(0)  # first element with this pattern is garbage
    widths[len(widths) - 1] += 1  # last element is off by one this way

    total = 0

    # iterate left to right through all the columns in one go
    cur_x = 0
    for i, op in enumerate(ops):
        width = widths[i]
        nums = [""] * width
        for x in range(cur_x, cur_x + width):
            for y in range(0, rows):
                nums[x - cur_x] += lines[y][x]
        if op == "+":
            total += sum([int(n) for n in nums])
        else:
            total += product([int(n) for n in nums])
        cur_x += width + 1

    return total


class Test(unittest.TestCase):
    example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

    def test_part1_example(self):
        input = self.example
        self.assertEqual(part1(input), 4277556)

    def test_part1_real(self):
        with open("inputs/day06.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(part1(input), 6417439773370)

    def test_part2_example(self):
        input = self.example
        self.assertEqual(part2(input), 3263827)

    def test_part2_real(self):
        with open("inputs/day06.txt", "r") as file:
            input = file.read()
        self.assertEqual(part2(input), 11044319475191)


if __name__ == "__main__":
    unittest.main()
