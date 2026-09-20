class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += (ord(s[i]) - ord('z') - 1) * (i+1) * -1

        return res