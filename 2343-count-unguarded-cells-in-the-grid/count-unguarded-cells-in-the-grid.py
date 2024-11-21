class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0 for i in range(n)] for j in range(m)]
        for i,j in guards:
            matrix[i][j] = 2

        for i,j in walls:
            matrix[i][j] = 2  

        directions = [(-1,0),(0,1),(1,0),(0,-1)]

        for gx,gy in guards:
            for dx,dy in directions:
                x,y = gx,gy

                while True:
                    x += dx
                    y += dy

                    if x < 0  or x >= m or y < 0 or  y >= n or matrix[x][y] == 2:
                        break

                    matrix[x][y] = 1   

        answer = 0

        for row in matrix:
            answer += row.count(0)

        return answer                       
