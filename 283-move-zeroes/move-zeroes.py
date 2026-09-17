class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = 0

        for i, val in enumerate(nums):
            if val != 0:
                nums[l], nums[i] = nums[i], nums[l]
                l+=1
        return nums