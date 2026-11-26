class Solution:
    def canAliceWin(self, n: int) -> bool:
        r = 10
        f = False
        while r>0:
            if n<r:
                return f
            n -= r
            f = not f
            r -= 1