class Solution:
    def minMoves(self, nums: list[int]) -> int:
        ans = sum(nums) - len(nums) * min(nums)
        return ans