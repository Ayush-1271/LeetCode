class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumDigit(n):
            s = 0
            while n>0:
                r = n%10
                n //= 10
                s += r
            return s
        
        for i, v in enumerate(nums):
            if i == sumDigit(v):
                return i
        return -1