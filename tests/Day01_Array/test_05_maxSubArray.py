import sys
import unittest

from src.Day01_Array.P05_maxSubArray import Solution


class TestMaxSubArray(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        output = 6
        self.assertEqual(sol.maxSubArray(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [1]
        output = 1
        self.assertEqual(sol.maxSubArray(nums), output)

    def test_simple_case3(self):
        sol = Solution()
        nums = [5,4,-1,7,8]
        output = 23
        self.assertEqual(sol.maxSubArray(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
