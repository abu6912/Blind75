import sys
import unittest

from src.Day01_Array.P04_productExceptSelf import Solution


class TestTwoSum(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [1,2,3,4]
        output = [24,12,8,6]
        self.assertCountEqual(sol.productExceptSelf(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [-1,1,0,-3,3]
        output = [0,0,9,0,0]
        self.assertCountEqual(sol.productExceptSelf(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
