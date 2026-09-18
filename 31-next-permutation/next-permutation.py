class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = -1

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                x = i
                break
        
        if x == -1:
            nums.reverse()
            return

        for i in range(len(nums)-1, -1, -1):
            if nums[i] > nums[x]:
                nums[i], nums[x] = nums[x], nums[i]
                break
        nums[x+1:] = reversed(nums[x+1:])