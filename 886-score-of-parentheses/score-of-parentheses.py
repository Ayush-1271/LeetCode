class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = 0
        c = 0
        
        for i in range(len(s)):
            if s[i] =='(':
                c+=1
            else:
                c-=1

                if s[i-1] == '(':
                    ans += 2**c
        return ans