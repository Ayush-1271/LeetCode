class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        m = float("-inf")
        s = 0

        for i in nums:
            s += i
            if m < s:
                m = s
            if s < 0:
                s = 0
        return m