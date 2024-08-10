class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        R = len(grid)
        C = len(grid[0])

        new_grid = [[0 for i in range(C * 3)] for j in range(R * 3)]

        for i in range(R):
            for j in range(C):
                if grid[i][j] == '\\':
                    new_row = i * 3
                    new_col = j * 3

                    new_grid[new_row][new_col] = 1
                    new_grid[new_row + 1][new_col + 1]  = 1
                    new_grid[new_row + 2][new_col + 2] = 1
                elif grid[i][j] == '/':
                    new_row = i * 3
                    new_col = j * 3
                    new_grid[new_row][new_col + 2] = 1
                    new_grid[new_row + 1][new_col + 1 ]= 1
                    new_grid[new_row + 2][new_col]= 1

        direction = [(1,0),(0,1),(0,-1),(-1,0)]  
        visited = set()          

        def inbound(row,col):
            return (row < R * 3) and (col < C * 3 )and row >= 0 and col >= 0

        def dfs(row,col):
            if not inbound(row,col):
                return

            if new_grid[row][col] == 1:
                return

            if (row,col) in visited:
                return

            visited.add((row,col))

            for deltax,deltay in direction:
                new_row = row + deltax
                new_col = col + deltay

                dfs(new_row,new_col)

            return

        answer = 0

        for i in range(R * 3):
            for j in range(C * 3):
                if (i,j) not in visited and new_grid[i][j] == 0:
                    answer += 1
                    dfs(i,j)  

        return answer                                






