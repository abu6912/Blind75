import sys
import unittest

from src.Day07_Matrix.P02_spiralOrder import Solution


class TestSpiralOrder(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        output = [1,2,3,6,9,8,7,4,5]
        self.assertEqual(sol.spiralOrder(matrix), output)

    def test_simple_case2(self):
        sol = Solution()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]
        ]
        output = [1,2,3,4,8,12,11,10,9,5,6,7]
        self.assertEqual(sol.spiralOrder(matrix), output)

    def test_simple_case3(self):
        sol = Solution()
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
            [13, 14, 15, 16],
            [17, 18, 19, 20],
            [21, 22, 23, 24]
        ]
        output = [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
        self.assertEqual(sol.spiralOrder(matrix), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
