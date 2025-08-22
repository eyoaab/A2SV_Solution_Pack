class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        MinR, MaxR, MinC, MaxC = 1000, -1, 1000, -1
        
        for i, row in enumerate(grid):
            for j, x in enumerate(row):
                if x == 0: 
                    continue

                MinR = min(MinR, i)
                MaxR = max(MaxR, i)
                MinC = min(MinC, j)
                MaxC = max(MaxC, j)

        return (MaxR - MinR + 1) * (MaxC - MinC + 1)

             