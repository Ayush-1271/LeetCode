class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        mi = float('inf')
        ma = 0
        for i in prices:
            if i<mi:
                mi = i
            ma = max(ma, i-mi)
        return ma