class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = nums[0]

        for i in range(1, len(nums)):
            n ^= nums[i]
        
        return n