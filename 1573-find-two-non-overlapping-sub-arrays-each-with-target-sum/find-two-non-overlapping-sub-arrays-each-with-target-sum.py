class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)
        d = {0:0}
        f = [float('inf')] * (n+1)
        s = 0
        ans = float('inf')

        for i, val in enumerate(arr, 1):

            s += val
            f[i] = f[i-1]
            r_s = s - target

            if r_s in d:

                l = d[r_s]
                c_l = i - l
                f[i] = min(f[i], c_l)
                ans = min(ans, f[l] + c_l)
                
            d[s] = i
        
        return -1 if ans==float('inf') else ans