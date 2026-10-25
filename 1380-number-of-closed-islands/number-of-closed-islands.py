class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        def dfs(r: int, c: int):
            grid[r][c] = 1

            if r > 0 and not grid[r - 1][c]: 
                dfs(r - 1, c)
            if r + 1 < m and not grid[r + 1][c]: 
                dfs(r + 1, c)
            if c > 0 and not grid[r][c - 1]: 
                dfs(r, c - 1)
            if c + 1 < n and not grid[r][c + 1]: 
                dfs(r, c + 1)

        for i in range(m):
            if not grid[i][0]: 
                dfs(i, 0)
            if not grid[i][n - 1]: 
                dfs(i, n - 1)

        for j in range(n):
            if not grid[0][j]: 
                dfs(0, j)
            if not grid[m - 1][j]: 
                dfs(m - 1, j)

        count = 0
        for i in range(1, m - 1):
            row = grid[i]
            for j in range(1, n - 1):
                if not row[j]:
                    count += 1
                    dfs(i, j)

        return count