#Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high = prices[0]
        low = prices[0]
        profit = 0
        for i in prices:
            if i < low:
                low = i
            if i > high:
                high = i
                if(high - low)>profit:
                    profit = high - low
        return profit
