class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if m * n != len(original):
            return []
        
        grid = [[0] * n for _ in range(m)]
        for i in range(len(original)):
            row = i // n
            col = i % n
            grid[row][col] = original[i]
        
        return grid