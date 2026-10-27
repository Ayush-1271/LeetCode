class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        ans = []

        s = '.' * n
        s2 = '#'*(n-1) + '.'

        ans.append(s)

        for i in range(m-1):
            ans.append(s2)
        
        return ans
