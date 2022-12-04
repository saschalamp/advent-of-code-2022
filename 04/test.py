import unittest

from main import (
    is_fully_contained,
    has_full_containment,
    as_tuple,
    describes_full_containment,
    count_full_containments,
    is_overlapping,
    describes_overlapping,
    count_overlapping_pairs
)

class TestIsFullyContained(unittest.TestCase):

    def test_trivial_case(self):
        actual = is_fully_contained((1, 1), (1, 1))
        self.assertTrue(actual)

    def test_trivial_case_not_containing(self):
        actual = is_fully_contained((1, 1), (2, 2))
        self.assertFalse(actual)

    def test_simple_case_upper_edge(self):
        actual = is_fully_contained((2, 2), (1, 2))
        self.assertTrue(actual)

    def test_simple_case_lower_edge(self):
        actual = is_fully_contained((1, 1), (1, 2))
        self.assertTrue(actual)

    def test_simple_case_in_between(self):
        actual = is_fully_contained((2, 2), (1, 3))
        self.assertTrue(actual)

class TestHasFullContainment(unittest.TestCase):

    def test_case_1(self):
        actual = has_full_containment((2, 2), (1, 3))
        self.assertTrue(actual)

    def test_case_2(self):
        actual = has_full_containment((1, 3), (2, 2))
        self.assertTrue(actual)

class TestAsTuple(unittest.TestCase):

    def test_as_tuple(self):
        self.assertEqual(as_tuple("4-7"), (4, 7))

class TestDescribesFullContainment(unittest.TestCase):

    def test_check_case_1(self):
        actual = describes_full_containment("2-4,6-8")
        self.assertFalse(actual)

    def test_check_case_2(self):
        actual = describes_full_containment("2-3,4-5")
        self.assertFalse(actual)

    def test_check_case_3(self):
        actual = describes_full_containment("5-7,7-9")
        self.assertFalse(actual)

    def test_check_case_4(self):
        actual = describes_full_containment("2-8,3-7")
        self.assertTrue(actual)

    def test_check_case_5(self):
        actual = describes_full_containment("6-6,4-6")
        self.assertTrue(actual)

    def test_check_case_6(self):
        actual = describes_full_containment("2-6,4-8")
        self.assertFalse(actual)

class TestCountFullContainments(unittest.TestCase):

    def test_case(self):
        input = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
        actual = count_full_containments(input)
        self.assertEqual(actual, 2)

class TestIsOverlapping(unittest.TestCase):

    def test_trivial(self):
        actual = is_overlapping((1, 1), (1, 1))
        self.assertTrue(actual)

    def test_trivial_not_overlapping(self):
        actual = is_overlapping((1, 1), (2, 2))
        self.assertFalse(actual)

    def test_simple_case_upper_edge(self):
        actual = is_overlapping((2, 2), (1, 2))
        self.assertTrue(actual)

    def test_simple_case_lower_edge(self):
        actual = is_overlapping((1, 1), (1, 2))
        self.assertTrue(actual)

    def test_simple_case_in_between(self):
        actual = is_overlapping((2, 2), (1, 3))
        self.assertTrue(actual)

    def test_true_overlapping(self):
        actual = is_overlapping((1, 3), (2, 4))
        self.assertTrue(actual)

class TestDescribesOverlapping(unittest.TestCase):

    def test_check_case_1(self):
        actual = describes_overlapping("2-4,6-8")
        self.assertFalse(actual)

    def test_check_case_2(self):
        actual = describes_overlapping("2-3,4-5")
        self.assertFalse(actual)

    def test_check_case_3(self):
        actual = describes_overlapping("5-7,7-9")
        self.assertTrue(actual)

    def test_check_case_4(self):
        actual = describes_overlapping("2-8,3-7")
        self.assertTrue(actual)

    def test_check_case_5(self):
        actual = describes_overlapping("6-6,4-6")
        self.assertTrue(actual)

    def test_check_case_6(self):
        actual = describes_overlapping("2-6,4-8")
        self.assertTrue(actual)

class TestCountOverlappingPairs(unittest.TestCase):

    def test_case(self):
        input = [
            "2-4,6-8",
            "2-3,4-5",
            "5-7,7-9",
            "2-8,3-7",
            "6-6,4-6",
            "2-6,4-8"
        ]
        actual = count_overlapping_pairs(input)
        self.assertEqual(actual, 4)

if __name__ == "__main__":
    unittest.main()
