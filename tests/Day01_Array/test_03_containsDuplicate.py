import sys
import unittest

from src.Day01_Array.P03_containsDuplicate import Solution


class TestContainsDuplicate(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [1,2,3,1]
        output = True
        self.assertEqual(sol.containsDuplicate(nums), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [1,2,3,4]
        output = False
        self.assertEqual(sol.containsDuplicate(nums), output)

    def test_simple_case3(self):
        sol = Solution()
        nums = [1,1,1,3,3,4,3,2,4,2]
        output = True
        self.assertEqual(sol.containsDuplicate(nums), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
