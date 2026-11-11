class Solution:
    def minimumCost(self, cost1: int, cost2: int, costBoth: int, need1: int, need2: int) -> int:
        c = min(need1, need2)
        rem1 = need1 - c
        rem2 = need2 - c

        return c*min(costBoth, cost1+cost2) + rem1*min(costBoth, cost1) + rem2*min(costBoth, cost2)