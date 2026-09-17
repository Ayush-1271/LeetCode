class Solution:
    def majorityElement(self, nums: list[int]) -> int:
            n = 0
            for i, v in enumerate(nums):
                if n ==0:
                    n = 1
                    m = v
                else:
                    if m == v:
                        n += 1
                    else:
                        n -= 1
            return m