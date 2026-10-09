class Solution:
    def minInsertions(self, s: str) -> int:
        c = 0
        ans = 0

        for i in s:
            if i == '(':
                if c % 2 == 1:
                    ans += 1
                    c -= 1
                c += 2
            else:
                c -= 1
                if c < 0:
                    ans += 1
                    c = 1

        return ans + c