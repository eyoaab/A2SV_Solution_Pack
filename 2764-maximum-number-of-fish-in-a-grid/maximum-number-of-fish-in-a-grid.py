class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        direction = [(0,1),(1,0),(-1,0),(0,-1)]

        def inbound(row,col):
            return 0 <= row < R and 0 <= col < C

        def dfs(row,col,store):
            visited.add((row,col))

            for rd,cd in direction:
                new_row = rd + row
                new_col = cd + col

                if inbound(new_row,new_col) and grid[new_row][new_col] and (new_row,new_col) not in visited:
                    score[0] += grid[new_row][new_col]
                    dfs(new_row,new_col,score)
            return score[0] 

        answer = 0
        for row in range(R):
            for col in range(C):
                if grid[row][col] != 0 and (row,col) not in visited:
                    score = [grid[row][col]]
                    answer = max(answer,dfs(row,col,score)) 
        return answer                           


        