class Solution:
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        pair = [0]*n
        stack = []

        for i in range(n):
            if s[i] == '(':
                stack.append(i)
            elif s[i] == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i

        ans = []
        i = 0 
        d = 1
        while 0 <= i < n:
            if s[i] == '(' or s[i] == ')':
                i = pair[i]
                d = -d
            else:
                ans.append(s[i])

            i += d
        
        return ''.join(ans)