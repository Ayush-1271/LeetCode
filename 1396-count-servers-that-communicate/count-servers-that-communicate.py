class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        m, n =len(grid), len(grid[0])

        c = [0]*m
        r = [0]*n

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c[i] += 1
                    r[j] += 1
        
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if c[i]>1 or r[j] > 1:
                        ans+=1
        
        return ans