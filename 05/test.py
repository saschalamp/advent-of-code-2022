from collections import deque

import unittest

from main import (
    generate_stacks,
    move_crate,
    move_multiple_crates,
    move_multiple_crates_in_order,
    determine_message,
    translate_step,
    solve_puzzle,
    solve_puzzle_2
)

class TestGenerateStacks(unittest.TestCase):

    def test_simple(self):
        input = [
            "[A]",
            " 1"
        ]
        expected = [
            deque(["A"])
        ]
        self.assertEqual(generate_stacks(input), expected)
    
    def test_multiple_elements_one_stack(self):
        input = [
            "[C]",
            "[B]",
            "[A]",
            " 1"
        ]
        expected = [
            deque(["A", "B", "C"])
        ]
        self.assertEqual(generate_stacks(input), expected)
    
    def test_multiple_stacks_one_element_per_stack(self):
        input = [
            "[A] [B] [C]",
            " 1   2   3"
        ]
        expected = [
            deque(["A"]),
            deque(["B"]),
            deque(["C"])
        ]
        self.assertEqual(generate_stacks(input), expected)
    
    def test_multiple_stacks_multiple_elements(self):
        input = [
            "[E] [I] [H]",
            "[D] [F] [G]",
            "[A] [B] [C]",
            " 1   2   3"
        ]
        expected = [
            deque(["A", "D", "E"]),
            deque(["B", "F", "I"]),
            deque(["C", "G", "H"])
        ]
        self.assertEqual(generate_stacks(input), expected)
    
    def test_multiple_stacks_multiple_elements_with_gap(self):
        input = [
            "[E]     [H]",
            "[D]     [G]",
            "[A] [B] [C]",
            " 1   2   3"
        ]
        expected = [
            deque(["A", "D", "E"]),
            deque(["B"]),
            deque(["C", "G", "H"])
        ]
        self.assertEqual(generate_stacks(input), expected)

    def test_case_1(self):
        input = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 "
        ]
        expected = [
            deque(["Z", "N"]),
            deque(["M", "C", "D"]),
            deque(["P"])
        ]
        self.assertEqual(generate_stacks(input), expected)

    def test_my_case(self):
        input = [
            "[J]             [F] [M]            ",
            "[Z] [F]     [G] [Q] [F]            ",
            "[G] [P]     [H] [Z] [S] [Q]        ",
            "[V] [W] [Z] [P] [D] [G] [P]        ",
            "[T] [D] [S] [Z] [N] [W] [B] [N]    ",
            "[D] [M] [R] [J] [J] [P] [V] [P] [J]",
            "[B] [R] [C] [T] [C] [V] [C] [B] [P]",
            "[N] [S] [V] [R] [T] [N] [G] [Z] [W]",
            " 1   2   3   4   5   6   7   8   9 "
        ]
        expected = [
            deque(["N", "B", "D", "T", "V", "G", "Z", "J"]),
            deque(["S", "R", "M", "D", "W", "P", "F"]),
            deque(["V", "C", "R", "S", "Z"]),
            deque(["R", "T", "J", "Z", "P", "H", "G"]),
            deque(["T", "C", "J", "N", "D", "Z", "Q", "F"]),
            deque(["N", "V", "P", "W", "G", "S", "F", "M"]),
            deque(["G", "C", "V", "B", "P", "Q"]),
            deque(["Z", "B", "P", "N"]),
            deque(["W", "P", "J"])
        ]
        self.assertEqual(generate_stacks(input), expected)
    
class TestMoveCrate(unittest.TestCase):

    def test_move(self):
        stacks = [
            deque(["A"]),
            deque(["B"])
        ]
        move_crate(stacks, 1, 2)
        expected_stacks = [
            deque([]),
            deque(["B", "A"])
        ]
        self.assertEqual(stacks, expected_stacks)

class TestMoveMultipleCrates(unittest.TestCase):

    def test_move(self):
        stacks = [
            deque(["A", "B", "C"]),
            deque([])
        ]
        move_multiple_crates(stacks, 3, 1, 2)
        expected_stacks = [
            deque([]),
            deque(["C", "B", "A"])
        ]
        self.assertEqual(stacks, expected_stacks)

class TestMoveMultipleCratesInOrder(unittest.TestCase):

    def test_move(self):
        stacks = [
            deque(["A", "B", "C"]),
            deque([])
        ]
        move_multiple_crates_in_order(stacks, 3, 1, 2)
        expected_stacks = [
            deque([]),
            deque(["A", "B", "C"])
        ]
        self.assertEqual(stacks, expected_stacks)

class TestDetermineMessage(unittest.TestCase):

    def test_determine_message(self):
        stacks = [
            deque(["C"]),
            deque(["M"]),
            deque(["P", "D", "N", "Z"])
        ]
        actual = determine_message(stacks)
        self.assertEqual(actual, "CMZ")

class TestTranslateStep(unittest.TestCase):

    def test_translate_step(self):
        step = "move 1 from 2 to 3"
        n, source, target = translate_step(step)
        self.assertEqual(n, 1)
        self.assertEqual(source, 2)
        self.assertEqual(target, 3)


class TestSolvePuzzle(unittest.TestCase):

    def test_solve_example(self):
        input = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]
        actual = solve_puzzle(input)
        self.assertEqual(actual, "CMZ")


class TestSolvePuzzle2(unittest.TestCase):

    def test_solve_example(self):
        input = [
            "    [D]    ",
            "[N] [C]    ",
            "[Z] [M] [P]",
            " 1   2   3 ",
            "",
            "move 1 from 2 to 1",
            "move 3 from 1 to 3",
            "move 2 from 2 to 1",
            "move 1 from 1 to 2"
        ]
        actual = solve_puzzle_2(input)
        self.assertEqual(actual, "MCD")

if __name__ == "__main__":
    unittest.main()
