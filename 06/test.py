import unittest

from main import (
    find_marker
)

class TestFindMarker(unittest.TestCase):

    def test_simplest_case(self):
        stream = "abcd"
        self.assertEqual(find_marker(stream, 4), 4)

    def test_first_letter_twice(self):
        stream = "aabcd"
        self.assertEqual(find_marker(stream, 4), 5)

    def test_first_letter_threetimes(self):
        stream = "aaabcd"
        self.assertEqual(find_marker(stream, 4), 6)

    def test_second_letter_twice(self):
        stream = "abbcde"
        self.assertEqual(find_marker(stream, 4), 6)

    def test_first_letter_is_third_letter(self):
        stream = "afabcde"
        self.assertEqual(find_marker(stream, 4), 5)

    def test_example_1(self):
        stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(find_marker(stream, 4), 7)

    def test_example_2(self):
        stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(find_marker(stream, 4), 5)

    def test_example_3(self):
        stream = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(find_marker(stream, 4), 6)

    def test_example_4(self):
        stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(find_marker(stream, 4), 10)

    def test_example_5(self):
        stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(find_marker(stream, 4), 11)

    def test_part_2_example_1(self):
        stream = "mjqjpqmgbljsphdztnvjfqwrcgsmlb"
        self.assertEqual(find_marker(stream, 14), 19)

    def test_part_2_example_2(self):
        stream = "bvwbjplbgvbhsrlpgdmjqwftvncz"
        self.assertEqual(find_marker(stream, 14), 23)

    def test_part_2_example_3(self):
        stream = "nppdvjthqldpwncqszvftbrmjlhg"
        self.assertEqual(find_marker(stream, 14), 23)

    def test_part_2_example_4(self):
        stream = "nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"
        self.assertEqual(find_marker(stream, 14), 29)

    def test_part_2_example_5(self):
        stream = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
        self.assertEqual(find_marker(stream, 14), 26)

if __name__ == "__main__":
    unittest.main()
