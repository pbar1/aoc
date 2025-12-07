import unittest


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


class Test(unittest.TestCase):
    example = """
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
""".strip()

    def test_part1_example(self):
        input = self.example
        self.assertEqual(part1(input), 4277556)

    def test_part1_real(self):
        with open("inputs/day06.txt", "r") as file:
            input = file.read().strip()
        self.assertEqual(part1(input), 6417439773370)


if __name__ == "__main__":
    unittest.main()
