class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        psc = {0:1}
        ps = c = 0

        for i in range(len(nums)):
            ps += nums[i]
            r = ps - k
            if r in psc:
                c += psc[r]
            psc[ps] = psc.get(ps, 0) + 1
        
        return c
