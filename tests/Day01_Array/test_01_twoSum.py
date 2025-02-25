import sys
import unittest

from src.Day01_Array.P01_twoSum import Solution


class TestTwoSum(unittest.TestCase):
    def test_simple_case(self):
        sol = Solution()
        nums = [2,7,11,15]
        target = 9
        output = [0,1]
        self.assertCountEqual(sol.twoSum(nums, target), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
