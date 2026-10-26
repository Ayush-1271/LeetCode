
from typing import List

class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()

        def dfs(i, j):
            stack = [(i, j)]
            visited.add((i, j))
            total = 0

            while stack:
                x, y = stack.pop()
                total += grid[x][y]

                for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nx, ny = x + dx, y + dy

                    if (0 <= nx < m and 0 <= ny < n
                        and grid[nx][ny] != 0
                        and (nx, ny) not in visited):

                        visited.add((nx, ny))
                        stack.append((nx, ny))

            return total

        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0 and (i, j) not in visited:
                    island_sum = dfs(i, j)

                    if island_sum % k == 0:
                        ans += 1

        return ans
