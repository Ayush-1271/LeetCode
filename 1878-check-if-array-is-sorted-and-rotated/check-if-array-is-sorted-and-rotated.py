class Solution:
    def check(self, nums: List[int]) -> bool:
        c = 0
        for i, val in enumerate(nums):
            if nums[i-1]>val:
                c+=1
        return c<=1