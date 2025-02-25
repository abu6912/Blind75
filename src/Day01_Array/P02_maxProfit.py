"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


class Solution(object):
    def maxProfit(self, prices: List[int]) -> int:
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for ind, price in enumerate(prices):
            if ind == 0:
                min_price = price
                continue
            profit = price - min_price
            max_profit = max(max_profit, profit)
            min_price = min(min_price, price)
        return max_profit
