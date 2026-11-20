class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1
        
        # For length 1, each number can start either an up or down transition
        up = [1] * m
        down = [1] * m
        
        for _ in range(n - 1):
            next_up = [0] * m
            next_down = [0] * m
            
            # Prefix sum of 'down' for transitions going up
            pref = 0
            for v in range(m):
                next_up[v] = pref
                pref = (pref + down[v]) % MOD
            
            # Suffix sum of 'up' for transitions going down
            suff = 0
            for v in range(m - 1, -1, -1):
                next_down[v] = suff
                suff = (suff + up[v]) % MOD
                
            up, down = next_up, next_down
            
        return (sum(up) + sum(down)) % MOD
