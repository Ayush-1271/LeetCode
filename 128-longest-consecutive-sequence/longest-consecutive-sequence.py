class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums)==0:
            return 0

        nums = set(nums)

        l = 1

        for i in nums:

            if i-1 not in nums:
                c = 1
                x = i
                
                while x+1 in nums:
                    x = x+1
                    c += 1
                l = max(l, c)
        return l