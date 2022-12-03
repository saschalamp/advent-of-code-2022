import unittest

from main import (
    Shape,
    get_outcome_score,
    get_round_score,
    get_total_score,
    pick,
    get_total_score_2
)

class TestGetOutcomeScore(unittest.TestCase):
    
    def test_tie(self):
        actual = get_outcome_score(Shape.ROCK, Shape.ROCK)
        self.assertEqual(actual, 3)
    
    def test_paper_beats_rock(self):
        actual = get_outcome_score(Shape.PAPER, Shape.ROCK)
        self.assertEqual(actual, 6)
    
    def test_rock_beaten_by_paper(self):
        actual = get_outcome_score(Shape.ROCK, Shape.PAPER)
        self.assertEqual(actual, 0)
    
    def test_rock_beats_scissors(self):
        actual = get_outcome_score(Shape.ROCK, Shape.SCISSORS)
        self.assertEqual(actual, 6)
    
    def test_scissors_beaten_by_rock(self):
        actual = get_outcome_score(Shape.SCISSORS, Shape.ROCK)
        self.assertEqual(actual, 0)
    
    def test_scissors_beats_paper(self):
        actual = get_outcome_score(Shape.SCISSORS, Shape.PAPER)
        self.assertEqual(actual, 6)
    
    def test_paper_beaten_by_scissors(self):
        actual = get_outcome_score(Shape.PAPER, Shape.SCISSORS)
        self.assertEqual(actual, 0)


class TestGetRoundScore(unittest.TestCase):
    
    def test_tie(self):
        actual = get_round_score(Shape.ROCK, Shape.ROCK)
        self.assertEqual(actual, 4)
    
    def test_paper_beats_rock(self):
        actual = get_round_score(Shape.PAPER, Shape.ROCK)
        self.assertEqual(actual, 8)
    
    def test_rock_beaten_by_paper(self):
        actual = get_round_score(Shape.ROCK, Shape.PAPER)
        self.assertEqual(actual, 1)
    
    def test_rock_beats_scissors(self):
        actual = get_round_score(Shape.ROCK, Shape.SCISSORS)
        self.assertEqual(actual, 7)
    
    def test_scissors_beaten_by_rock(self):
        actual = get_round_score(Shape.SCISSORS, Shape.ROCK)
        self.assertEqual(actual, 3)
    
    def test_scissors_beats_paper(self):
        actual = get_round_score(Shape.SCISSORS, Shape.PAPER)
        self.assertEqual(actual, 9)
    
    def test_paper_beaten_by_scissors(self):
        actual = get_round_score(Shape.PAPER, Shape.SCISSORS)
        self.assertEqual(actual, 2)


class TestGetTotalScore(unittest.TestCase):
    
    def test_simple(self):
        actual = get_total_score(["A Z"])
        self.assertEqual(actual, 3)
    
    def test_example(self):
        actual = get_total_score(["A Y", "B X", "C Z"])
        self.assertEqual(actual, 15)


class TestPick(unittest.TestCase):

    def test_should_lose_against_rock(self):
        actual = pick(Shape.ROCK, "X")
        self.assertEqual(actual, Shape.SCISSORS)

    def test_should_tie_against_rock(self):
        actual = pick(Shape.ROCK, "Y")
        self.assertEqual(actual, Shape.ROCK)

    def test_should_win_against_rock(self):
        actual = pick(Shape.ROCK, "Z")
        self.assertEqual(actual, Shape.PAPER)

class TestGetTotalScore2(unittest.TestCase):
    
    def test_example(self):
        actual = get_total_score_2(["A Y", "B X", "C Z"])
        self.assertEqual(actual, 12)


if __name__ == "__main__":
    unittest.main()
