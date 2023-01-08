import unittest
from os import path

from solution import *


class TestChallenge(unittest.TestCase):
    def setUp(self):
        file_path = path.abspath(__file__)
        dir_path = path.dirname(file_path)
        self.test_file_path = path.join(dir_path,'test_input.txt')

    def test_first_challenge(self):
        expected = 15
        actual = solve_challenge(self.test_file_path)

        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
