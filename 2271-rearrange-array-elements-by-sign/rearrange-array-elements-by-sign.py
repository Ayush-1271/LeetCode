class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        p, n = 0, 1
        arr = [0] * len(nums)
        for i in nums:
            if i > 0:
                arr[p] = i
                p +=2
            if i < 0:
                arr[n] = i
                n += 2
        return arr