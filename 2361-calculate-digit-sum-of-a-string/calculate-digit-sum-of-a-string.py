class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            ans = ""

            for i in range(0, len(s), k):
                ans += str(sum(int(x) for x in s[i:i+k]))

            s = ans

        return s