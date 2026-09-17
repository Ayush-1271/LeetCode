class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        max_1, c_1 = 0, 0

        for i in nums:
            if i == 1:
                c_1+=1
            else:
                max_1 = max(max_1, c_1)
                c_1 = 0
        
        return max(max_1, c_1)