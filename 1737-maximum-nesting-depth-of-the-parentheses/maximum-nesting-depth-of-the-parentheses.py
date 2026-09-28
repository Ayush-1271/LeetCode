class Solution:
    def maxDepth(self, s: str) -> int:
        '''
        # Method 1:: using stack
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
        
        return m'''
        # Method 2:: using counter

        m = 0
        c = 0
        for i in s:
            if i == '(':
                c+= 1
            elif i == ')':
                c-= 1
            else:
                pass
            m = max(m, c)
        
        return m