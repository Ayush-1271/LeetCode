class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        t = sum(nums) - x
        if t < 0:
            return -1

        if t == 0:
            return len(nums)

        ans = self._cal(nums, t)

        return len(nums) - ans if ans != 0 else -1

        
    def _cal(self, arr: list[int], k:int) ->int:
        n = len(arr)
        l = s = ml = 0

        for r in range(n):
            s+= arr[r]
            while s > k:
                s -= arr[l]
                l += 1
            if s==k:
                ml = max(ml, r-l+1)
        return ml
