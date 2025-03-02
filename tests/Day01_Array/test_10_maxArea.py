import sys
import unittest

from src.Day01_Array.P10_maxArea import Solution


class TestMaxArea(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
        output = 49
        self.assertEqual(sol.maxArea(height), output)

    def test_simple_case2(self):
        sol = Solution()
        height = [1, 1]
        output = 1
        self.assertEqual(sol.maxArea(height), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
