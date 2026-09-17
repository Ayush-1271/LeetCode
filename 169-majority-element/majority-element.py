class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        def find():
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
        
        c, t = 0, find()
        for i in nums:
            if i == t:
                c += 1

        if c > len(nums)//2:
            return t