class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        ans = 0
        startX, startY = 0,0
        row, col = len(board), len(board[0])

        # to get the starting point
        for i in range(0,row):
            for j in range(col):
                if board[i][j] == 'R':
                    startX, startY = i, j
                    break
        # 1
        for i in range(startX, row):
            if board[i][startY] == 'p':
                ans += 1
                break 
            elif board[i][startY] == 'B':
                break
        # 2
        for i in range(startX, -1, -1):
            if board[i][startY] == 'p':
                ans += 1
                break
            elif board[i][startY] == 'B':
                break 
        
            #3   
        for i in range(startY, col):
            if board[startX][i] == 'p':
                ans += 1
                break 
            elif board[startX][i]  == 'B':
                break 
    #    4
        for i in range(startY, -1, -1):
            if board[startX][i] == 'p':
                ans += 1
                break
            elif board[startX][i] == 'B':
                break  

        return ans        