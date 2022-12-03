import unittest

from main import determine_most_calories

class TestDetermineMostCalories(unittest.TestCase):

    def test_single_elf_single_value(self):
        actual = determine_most_calories(["42"])
        self.assertEqual(actual, [42])

    def test_single_elf_multiple_values(self):
        actual = determine_most_calories(["42", "1337"])
        self.assertEqual(actual, [1379])

    def test_two_elves_multiple_values(self):
        actual = determine_most_calories(["42", "1337", "", "815", "4711"])
        self.assertEqual(actual, [5526, 1379])

    def test_three_elves_multiple_values(self):
        actual = determine_most_calories(["42", "1337", "", "815", "4711", "", "420", "69"])
        self.assertEqual(actual, [5526, 1379, 489])

    def test_four_elves_multiple_values(self):
        actual = determine_most_calories(["42", "1337", "", "815", "4711", "", "420", "69", "", "123", "456", "789"])
        self.assertEqual(actual, [5526, 1379, 1368])

if __name__ == "__main__":
    unittest.main()
