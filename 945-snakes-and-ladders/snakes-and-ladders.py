class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        board.reverse()
        N= len(board)
        answer = []
        visitd = set()
        queue = deque()#row,col ,step
        queue.append([1,0])#num,step
        visitd.add(1)

        def helper(val):
            row = (val-1)//N
            col = (val-1)%N
            if row %2:
                col = N-1-col
            return (row,col) 

        ans = float("inf")
        while queue:
            n = len(queue)
            for i in range(n):
                val,step = queue.popleft()
                if val == N*N:
                    ans = min(ans,step)
                for j in range(val+1,min((N*N),val+6)+1):
                    new_row,new_col = helper(j)
                    if ((j) not in visitd):
                        visitd.add(j)
                        
                        if board[new_row][new_col] != -1: 
                            val2 = board[new_row][new_col]
                            queue.append([val2,step+1])
                            
                                   
                        else:
                            queue.append([j,step+1])
                         
        return -1 if ans == float("inf") else ans



        