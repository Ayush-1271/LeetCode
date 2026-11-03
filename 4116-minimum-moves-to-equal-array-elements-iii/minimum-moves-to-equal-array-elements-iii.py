class Solution:
    def minMoves(self, nums: List[int]) -> int:
        a = max(nums)

        ans = 0
        for i in nums:
            ans += abs(i-a)
        
        return ans