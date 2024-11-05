class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        row = [len(mat[0]) for i in range(len(mat))]
        col = [len(mat) for i in range(len(mat[0]))]
        store = {}

        for i in range(len(row)):
            for j in range(len(col)):
                store[mat[i][j]] = [i,j]

        for index,value in enumerate(arr):
            removedRow,removedCol = store[value]  
            row[removedRow] -= 1
            col[removedCol] -= 1   

            if row[removedRow]  == 0 or   col[removedCol] == 0:
                return index

        return len(arr)         

                
        