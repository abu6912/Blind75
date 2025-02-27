import sys
import unittest

from src.Day07_Matrix.P04_exist import Solution


class TestSpiralOrder(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCCED"
        output = True
        self.assertEqual(sol.exist(board, word), output)

    def test_simple_case2(self):
        sol = Solution()
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "SEE"
        output = True
        self.assertEqual(sol.exist(board, word), output)

    def test_simple_case3(self):
        sol = Solution()
        board = [
            ["A", "B", "C", "E"],
            ["S", "F", "C", "S"],
            ["A", "D", "E", "E"]
        ]
        word = "ABCB"
        output = False
        self.assertEqual(sol.exist(board, word), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
