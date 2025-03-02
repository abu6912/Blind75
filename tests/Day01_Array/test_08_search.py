import sys
import unittest

from src.Day01_Array.P08_search import Solution


class TestSearch(unittest.TestCase):
    def test_simple_case1(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 0
        output = 4
        self.assertEqual(sol.search(nums, target), output)

    def test_simple_case2(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 3
        output = -1
        self.assertEqual(sol.search(nums, target), output)

    def test_simple_case3(self):
        sol = Solution()
        nums = [1]
        target = 0
        output = -1
        self.assertEqual(sol.search(nums, target), output)

    def test_simple_case4(self):
        sol = Solution()
        nums = [4, 5, 6, 7, 0, 1, 2]
        target = 5
        output = 1
        self.assertEqual(sol.search(nums, target), output)

    def test_simple_case5(self):
        sol = Solution()
        nums = [1, 3, 5]
        target = 0
        output = -1
        self.assertEqual(sol.search(nums, target), output)


if __name__ == "__main__":
    unittest.main()
    sys.exit(0)
