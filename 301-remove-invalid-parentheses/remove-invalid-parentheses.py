class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:

        left = 0
        right = 0

        for i in s:
            if i == '(':
                left += 1
            elif i == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1

        ans = set()

        def backtrack(i, balance, l, r, cur):

            if i == len(s):
                if balance == 0 and l == 0 and r == 0:
                    ans.add(''.join(cur))
                return

            if s[i] == '(':

                # Remove '('
                if l > 0:
                    backtrack(i + 1, balance, l - 1, r, cur)

                # Keep '('
                cur.append('(')
                backtrack(i + 1, balance + 1, l, r, cur)
                cur.pop()

            elif s[i] == ')':

                # Remove ')'
                if r > 0:
                    backtrack(i + 1, balance, l, r - 1, cur)

                # Keep ')' 
                if balance > 0:
                    cur.append(')')
                    backtrack(i + 1, balance - 1, l, r, cur)
                    cur.pop()

            else:
                cur.append(s[i])
                backtrack(i + 1, balance, l, r, cur)
                cur.pop()

        backtrack(0, 0, left, right, [])

        return list(ans)