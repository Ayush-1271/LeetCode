class Solution:
    def gcd(self, a: int, b: int) -> int:
        if b == 0:
            return a
        return self.gcd(b, a % b)
    
    def lcm(self, a: int, b: int) -> int:
        if a == 0 or b == 0:
            return 0
        return abs(a // self.gcd(a, b) * b)

    def maxLength(self, nums: List[int]) -> int:
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            p = 1
            g = 0
            l = 1
            for j in range(i, n):
                p *= nums[j]
                g = self.gcd(g, nums[j])
                l = self.lcm(l, nums[j])
                
                if p == l * g:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len
