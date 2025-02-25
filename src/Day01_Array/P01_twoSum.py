"""
https://leetcode.com/problems/two-sum/description/
"""
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map_dict = {}
        for ind, num in enumerate(nums):
            rest = target - num
            if rest in map_dict.keys():
                return [ind, map_dict[rest]]
            else:
                map_dict[num] = ind
        return [-1, -1]
