class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        def find(n):
            s, e = 0, len(n)-1
            while s<e:
                if n[s]+n[e] == target:
                    return n[s], n[e]
                elif n[s]+n[e] < target:
                    s+=1
                else:
                    e-=1
        n1, n2 = find(sorted(nums))
        res = [None, None]
        for i, v in enumerate(nums):
            if v == n1 and res[0] == None:
                res[0] = i
            elif v == n2:
                res[1] = i
        return res