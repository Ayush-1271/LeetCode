class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []
        m = 0
        for i in s:
            if i == '(':
                stack.append(i)
            elif i == ')':
                stack.pop()
            else:
                pass
            m = max(m, len(stack))
        
        return m