class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        N,M = len(grid),len(grid[0])
        differance = [[0 for i in range(M) ]for j in range(N)]

        zeroCol = [0 for i in range(M)]
        zeroRow = [0 for i in range(N)]

        oneCol = [0 for i in range(M)]
        oneRow = [0 for i in range(N)]


        for row in range(N):
            for col in range(M):
                if grid[row][col]:
                    oneRow[row] += 1
                    oneCol[col] += 1
                else:
                    zeroRow[row] += 1
                    zeroCol[col] += 1  

        for row in range(N):
            for col in range(M):   
                differance[row][col] =   oneRow[row]  + oneCol[col]  - zeroRow[row] -  zeroCol[col]        

        return differance



