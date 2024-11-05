class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n = len(grid[0])

        top = [0] * n
        top[0] = grid[0][0]
        for i in range(1, n):
            top[i] = top[i - 1] + grid[0][i]
        
        bottom = [0] * n
        bottom[-1] = grid[1][-1]
        for i in range(n - 2, -1, -1):
            bottom[i] = bottom[i + 1] + grid[1][i]
        
        answer = float('inf')

        for i in range(n):
            score = max(top[-1] - top[i] , bottom[0] - bottom[i])
            answer = min(answer, score)
        
        return answer
