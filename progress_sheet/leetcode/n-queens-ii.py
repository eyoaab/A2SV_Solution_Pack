class Solution:
    def totalNQueens(self, n: int) -> int:
        answer=[]
        column=set()
        posetive_diag=set()
        negative_diag=set()
        table=[['.']*n for i in range(n)]

        def backtrack(row):
            if row==n:
                temp=["".join(col) for col in table]
                answer.append(temp)
                return
            for col in range(n):
                if (row+col) in posetive_diag or (row-col) in negative_diag or col in column:
                    continue
                column.add(col)
                posetive_diag.add(row+col)
                negative_diag.add(row-col)
                table[row][col]='Q'

                backtrack(row+1)

                column.remove(col)
                posetive_diag.remove(row+col)
                negative_diag.remove(row-col)
                table[row][col]='.'
        backtrack(0)
        return len(answer)        






        
        