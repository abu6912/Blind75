import sys
import unittest

from src.Day01_Array.P02_maxProfit import Solution


class TestTwoSum(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        prices = [7, 1, 5, 3, 6, 4]
        output = 5
        self.assertEqual(sol.maxProfit(prices), output)

    def test_simple_case2(self):
        sol = Solution()
        prices = [7, 6, 4, 3, 1]
        output = 0
        self.assertEqual(sol.maxProfit(prices), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
