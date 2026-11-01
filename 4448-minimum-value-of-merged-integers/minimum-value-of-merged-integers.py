class Solution:
    def minMergedInteger(self, nums: list[int]) -> int:
        m = []

        for i in range(0, len(nums), 2):
            m.append(int(str(nums[i]) + str(nums[i+1])))
        
        return min(m)