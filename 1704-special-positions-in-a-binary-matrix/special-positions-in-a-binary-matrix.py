class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
            N,M = len(mat),len(mat[0])
            differance = [[0 for i in range(M) ]for j in range(N)]

            oneCol = [0 for i in range(M)]
            oneRow = [0 for i in range(N)]

            ans = 0


            for row in range(N):
                for col in range(M):
                    if mat[row][col]:
                        oneRow[row] += 1
                        oneCol[col] += 1
                  

            for row in range(N):
                for col in range(M):   
                    ans += mat[row][col] == 1 and  oneRow[row] == 1 and oneCol[col] == 1    

            return ans