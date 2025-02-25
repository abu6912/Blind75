"""
https://leetcode.com/problems/product-of-array-except-self/
"""
from typing import List


class Solution(object):
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left = [1]* len(nums)
        right = [1]* len(nums)
        for ind, num in enumerate(nums):
            if ind == 0:
                continue
            left[ind] *= left[ind-1] * nums[ind-1]
        for ind in range(len(nums)-1, -1, -1):
            if ind == len(nums)-1:
                continue
            right[ind] *= right[ind+1] * nums[ind+1]

        temp = []
        for ind in range(len(nums)):
            temp.append(left[ind] * right[ind])
        return temp
