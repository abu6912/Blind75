import sys
import unittest

from src.Day01_Array.P06_maxProduct import Solution


class TestMaxProduct(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [2, 3, -2, 4]
        output = 6
        self.assertEqual(sol.maxProduct(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [-2, 0, -1]
        output = 0
        self.assertEqual(sol.maxProduct(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
