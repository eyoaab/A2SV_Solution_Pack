class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        maxRow, maxCol = len(grid), len(grid[0])
        visited = set()

        if grid[0][0] == ")" or grid[maxRow -1][maxCol -1] == "(":
            return False
            

        def dfs(row,col,balance):
            if row >= maxRow or col >= maxCol:
                return False
            char = grid[row][col]


            if char == ")":
                balance -= 1
            else:
                balance += 1 

            if balance < 0:
                return False

            if row == maxRow - 1 and col == maxCol -1:
                return balance == 0    

            state = (row,col,balance)

            if state in visited:
                return False
            visited.add(state)

            return (dfs(row,col + 1,balance) or dfs(row + 1,col,balance))  

        return dfs(0,0,0)                  