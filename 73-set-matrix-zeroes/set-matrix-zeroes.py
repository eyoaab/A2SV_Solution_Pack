class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        removableCols = set()
        removableRows = set()
        rows = len(matrix)
        cols = len(matrix[0])


        for i in range(rows):
            for j in range(cols):

                if matrix[i][j] == 0:
                    removableCols.add(j)
                    removableRows.add(i)

        for i in range(rows):
            for j in range(cols):
                if i in removableRows or j in removableCols:
                    matrix[i][j] = 0


        