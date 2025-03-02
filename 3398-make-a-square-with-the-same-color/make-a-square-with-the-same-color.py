class Solution:
    def canMakeSquare(self, grid: List[List[str]]) -> bool:
        def count(x, y):
            colors = [grid[x][y], grid[x][y+1], grid[x+1][y], grid[x+1][y+1]]
            count = {'B': 0, 'W': 0}
            for c in colors:
                count[c] += 1
            return count['B'] >= 3 or count['W'] >= 3

        for i in range(2):
            for j in range(2):
                if count(i, j):
                    return True
        return False