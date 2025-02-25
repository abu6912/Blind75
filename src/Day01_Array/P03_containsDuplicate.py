"""
https://leetcode.com/problems/contains-duplicate/
"""
from typing import List


class Solution(object):
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        for ind in range(1, len(nums)):
            if nums[ind] == nums[ind-1]:
                return True
        return False
