class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        store = {}

        for i in range(n):
            for j in range(m):
                key = i - j
                if key not in store: 
                    store[key] = []
                if key < 0: 
                    heappush(store[key], grid[i][j])
                else: 
                    heappush(store[key], -grid[i][j])

        for i in range(n):
            for j in range(m):
                key = i - j
                if key < 0: 
                    grid[i][j] = heappop(store[key])
                else: 
                    grid[i][j] = -heappop(store[key])
        
        return grid