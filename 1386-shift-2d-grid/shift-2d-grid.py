class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n, ans = len(grid), len(grid[0]), []
        
        for i in range(m):
            ans.append([])
            for j in range(n):
                d = (i * n + j - k) % (m * n)
                ans[-1].append(grid[d//n][d%n])
        return ans