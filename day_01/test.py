import unittest
from os import path

from solution import *


class TestChallenge(unittest.TestCase):

    def test_first_challenge(self):
        file_path = path.abspath(__file__)
        dir_path = path.dirname(file_path)
        test_file_path = path.join(dir_path,'test_input.txt')

        expected = 24000

        actual = solve_challenge(test_file_path)

        self.assertEqual(actual, expected)

if __name__ == '__main__':
    unittest.main()
