class Solution:
    def checkString(self, s: str) -> bool:
        f = False
        for i in s:
            if i == 'b':
                f = True
            if f:
                if i == 'a':
                    return False
        
        return True