class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c = 0
        l = list(s)
        for i, v in enumerate(s):
            if v == '(':
                if c==0:
                    l[i] = ''
                c+=1
            else:
                c-= 1
                if c == 0:
                    l[i] = ''
            
        return ''.join(l)