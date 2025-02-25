import sys
import unittest

from src.Day07_Matrix.P03_rotate import Solution


class TestSpiralOrder(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ]
        output = [
            [7, 4, 1],
            [8, 5, 2],
            [9, 6, 3]
        ]
        sol.rotate(matrix)
        self.assertEqual(matrix, output)

    def test_simple_case2(self):
        sol = Solution()
        matrix = [
            [5, 1, 9, 11],
            [2, 4, 8, 10],
            [13, 3, 6, 7],
            [15, 14, 12, 16]
        ]
        output = [
            [15, 13, 2, 5],
            [14, 3, 4, 1],
            [12, 6, 8, 9],
            [16, 7, 10, 11]
        ]
        sol.rotate(matrix)
        self.assertEqual(matrix, output)

    # def test_simple_case3(self):
    #     sol = Solution()
    #     matrix = [
    #         [1, 2, 3, 4],
    #         [5, 6, 7, 8],
    #         [9, 10, 11, 12],
    #         [13, 14, 15, 16],
    #         [17, 18, 19, 20],
    #         [21, 22, 23, 24]
    #     ]
    #     output = [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
    #     self.assertEqual(sol.rotate(matrix), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
