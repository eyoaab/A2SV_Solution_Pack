MOD = 10**9 + 7

class Solution:
    def numberOfPaths(self, grid: List[List[int]], k: int) -> int:
        @cache
        def dfs(r, c, total):
            if r == row - 1 and c == col - 1:
                return 0 if total else 1
            res = 0
            for dr, dc in ((1, 0), (0, 1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    res += dfs(nr, nc, (total + grid[nr][nc]) % k)
            return res % MOD

        row, col = len(grid), len(grid[0])
        return dfs(0, 0, grid[0][0] % k)
        