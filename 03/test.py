import unittest

from main import (
    get_same_item,
    get_priority,
    get_rucksack_priority,
    get_total_priority,
    get_badge,
    get_total_badge_priority
)

class TestGetSameItems(unittest.TestCase):

    def test_simple_case(self):
        actual = get_same_item("a", "a")
        self.assertEqual(actual, "a")

    def test_simple_case_no_same_items(self):
        actual = get_same_item("a", "b")
        self.assertEqual(actual, None)

    def test_two_items_each_one_same_item(self):
        actual = get_same_item("ac", "ba")
        self.assertEqual(actual, "a")

    def test_case_1(self):
        actual = get_same_item("vJrwpWtwJgWr", "hcsFMMfFFhFp")
        self.assertEqual(actual, "p")

    def test_case_2(self):
        actual = get_same_item("jqHRNqRjqzjGDLGL", "rsFMfFZSrLrFZsSL")
        self.assertEqual(actual, "L")

class TestGetPriority(unittest.TestCase):

    def test_a(self):
        self.assertEqual(get_priority("a"), 1)

    def test_b(self):
        self.assertEqual(get_priority("b"), 2)

    def test_z(self):
        self.assertEqual(get_priority("z"), 26)

    def test_A(self):
        self.assertEqual(get_priority("A"), 27)

    def test_B(self):
        self.assertEqual(get_priority("B"), 28)

    def test_Z(self):
        self.assertEqual(get_priority("Z"), 52)

class TestGetRucksackPriority(unittest.TestCase):
    
    def test_case_1(self):
        priority = get_rucksack_priority("vJrwpWtwJgWrhcsFMMfFFhFp")
        self.assertEqual(priority, 16)
    
    def test_case_2(self):
        priority = get_rucksack_priority("jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL")
        self.assertEqual(priority, 38)
    
    def test_case_3(self):
        priority = get_rucksack_priority("PmmdzqPrVvPwwTWBwg")
        self.assertEqual(priority, 42)
    
    def test_case_4(self):
        priority = get_rucksack_priority("wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn")
        self.assertEqual(priority, 22)
    
    def test_case_5(self):
        priority = get_rucksack_priority("ttgJtRGJQctTZtZT")
        self.assertEqual(priority, 20)
    
    def test_case_6(self):
        priority = get_rucksack_priority("CrZsJsPPZsGzwwsLwLmpwMDw")
        self.assertEqual(priority, 19)

class TestGetTotalPriority(unittest.TestCase):

    def test_example(self):
        input = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        priority = get_total_priority(input)
        self.assertEqual(priority, 157)

class TestGetBatch(unittest.TestCase):

    def test_simple(self):
        input = [
            "ab",
            "ac",
            "ad"
        ]
        priority = get_badge(input)
        self.assertEqual(priority, "a")

    def test_no_batch(self):
        input = [
            "ab",
            "cd",
            "ef"
        ]
        priority = get_badge(input)
        self.assertEqual(priority, None)

    def test_b(self):
        input = [
            "ab",
            "bc",
            "db"
        ]
        priority = get_badge(input)
        self.assertEqual(priority, "b")

    def test_case_1(self):
        input = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg"
        ]
        priority = get_badge(input)
        self.assertEqual(priority, "r")

    def test_case_2(self):
        input = [
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        priority = get_badge(input)
        self.assertEqual(priority, "Z")

class TestGetTotalBatchPriority(unittest.TestCase):

    def test_example(self):
        input = [
            "vJrwpWtwJgWrhcsFMMfFFhFp",
            "jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
            "PmmdzqPrVvPwwTWBwg",
            "wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
            "ttgJtRGJQctTZtZT",
            "CrZsJsPPZsGzwwsLwLmpwMDw"
        ]
        priority = get_total_badge_priority(input)
        self.assertEqual(priority, 70)

if __name__ == "__main__":
    unittest.main()
