class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(l : int, r: int, s: str) -> None:
            if l>n or r>n or l<r:
                return
            if l == n and r==n:
                res.append(s)
                return
            generate(l+1, r, s+'(')
            generate(l, r+1, s+')')
        
        res = []
        generate(0, 0, '')
        return res