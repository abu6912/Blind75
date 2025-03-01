import sys
import unittest

from src.Day01_Array.P09_threeSum import Solution


class TestFindMin(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [-1, 0, 1, 2, -1, -4]
        output = [[-1, -1, 2], [-1, 0, 1]]
        self.assertCountEqual(sol.threeSum(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [0, 1, 1]
        output = []
        self.assertEqual(sol.threeSum(nums), output)

    def test_simple_case3(self):
        sol = Solution()
        nums = [0, 0, 0]
        output = [[0, 0, 0]]
        self.assertEqual(sol.threeSum(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
