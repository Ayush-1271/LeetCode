class Solution:

    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        memo = {}

        if (m + n - 1) % 2:
            return False

        def solve(i, j, b):

            if i >= m or j >= n:
                return False

            # Process current cell
            if grid[i][j] == '(':
                b += 1
            else:
                b -= 1

            # Invalid prefix
            if b < 0:
                return False

            # Reached destination
            if i == m - 1 and j == n - 1:
                return b == 0

            key = (i, j, b)

            if key in memo:
                return memo[key]

            memo[key] = (
                solve(i + 1, j, b) or
                solve(i, j + 1, b)
            )

            return memo[key]

        return solve(0, 0, 0)