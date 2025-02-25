import sys
import unittest

from src.Day01_Array.P07_findMin import Solution


class TestFindMin(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [3, 4, 5, 1, 2]
        output = 1
        self.assertEqual(sol.findMin(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        output = 0
        self.assertEqual(sol.findMin(nums), output)

    def test_simple_case3(self):
        sol = Solution()
        nums = [11, 13, 15, 17]
        output = 11
        self.assertEqual(sol.findMin(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
