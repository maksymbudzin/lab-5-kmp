import unittest

from kmp import kmp_algorithm


class Test_kmp(unittest.TestCase):

    def test_first_case(self):
        text = "mmm"
        pattern = "mm"
        matches = kmp_algorithm(text, pattern)
        self.assertEqual(
            [(0, 1), (1, 2)],
            matches
        )

    def test_second_case(self):
        text = "zzizzz"
        pattern = "zz"
        matches = kmp_algorithm(text, pattern)
        self.assertEqual(
            [(0, 1), (3, 4), (4, 5)],
            matches
        )

    def test_third_case(self):
        text = "bbbabbbb"
        pattern = "bbb"
        matches = kmp_algorithm(text, pattern)
        self.assertEqual(
            [(0, 2), (4, 6), (5, 7)],
            matches
        )

    def test_fourth_case(self):
        text = "wassdvsasdffrhbcwsadwadsvseafrhbfvbdfs"
        pattern = "frhb"
        matches = kmp_algorithm(text, pattern)
        self.assertEqual(
            [(11, 14), (28, 31)],
            matches
        )

    def test_empty_pattern(self):
        text = "lviv"
        pattern = ""
        self.assertRaises(
            ValueError,
            kmp_algorithm, text, pattern
        )

    def test_empty_text(self):
        text = ""
        pattern = "maks"
        self.assertRaises(
            ValueError,
            kmp_algorithm, text, pattern
        )

    def test_pattern_longer_that_text(self):
        text = "maks"
        pattern = "maksym"
        self.assertRaises(
            ValueError,
            kmp_algorithm, text, pattern
        )

    def test_wrong_inputs(self):
        text1 = 2
        pattern1 = "maks"
        self.assertRaises(
            ValueError,
            kmp_algorithm, text1, pattern1
        )

        text2 = "maks"
        pattern2 = 5
        self.assertRaises(
            ValueError,
            kmp_algorithm, text2, pattern2
        )

        text3 = 7
        pattern3 = 9
        self.assertRaises(
            ValueError,
            kmp_algorithm, text3, pattern3
        )
