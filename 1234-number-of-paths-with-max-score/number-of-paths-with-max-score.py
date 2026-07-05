class Solution:
    def pathsWithMaxScore(self, board):
        board[0] = board[0].replace("E","0")
        board[-1] = board[-1].replace("S","0")

        m, n, mod = len(board), len(board[0]), 10**9+7

        @lru_cache(None)
        def function(i,j):
            if i >= m or j >= n or board[i][j] == "X":
                return (float("-inf"),0)

            if i == m-1 and j == n-1:
                return (0,1)

            op1 = function(i+1,j)
            op2 = function(i,j+1)
            op3 = function(i+1,j+1)

            score = int(board[i][j])

            count, prev_score = 0, max(op1[0],op2[0],op3[0])

            if op1[0] == prev_score:
                count += op1[1]

            if op2[0] == prev_score:
                count += op2[1]

            if op3[0] == prev_score:
                count += op3[1]

            return (score+prev_score,count%mod)
        
        res = function(0,0)

        return [max(res[0],0),res[1]]