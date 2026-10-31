class Solution:
    def uniquePaths(self, g: List[List[int]]) -> int:
        m = len(g)
        n = len(g[0])
        M = 10**9 + 7
        
        # L: arrived moving right, T: arrived moving down
        L = [[0] * n for _ in range(m)]
        T = [[0] * n for _ in range(m)]
        
        L[0][0] = 1
        
        for i in range(m):
            for j in range(n):
                # from the left: T always, L if no mirror
                if j > 0:
                    L[i][j] = T[i][j - 1]
                    if g[i][j - 1] == 0:
                        L[i][j] += L[i][j - 1]
                
                # from the top: L always, T if no mirror
                if i > 0:
                    T[i][j] = L[i - 1][j]
                    if g[i - 1][j] == 0:
                        T[i][j] += T[i - 1][j]
                
                L[i][j] %= M
                T[i][j] %= M
                
        return (L[m - 1][n - 1] + T[m - 1][n - 1]) % M
