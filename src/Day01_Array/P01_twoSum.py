"""
https://leetcode.com/problems/two-sum/description/
"""

class Solution(object):
    def twoSum(self, nums, target):
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
