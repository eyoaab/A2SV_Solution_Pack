class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
       
        freshs = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    freshs+=1
                if grid[i][j] == 2:
                    queue.append((i,j))
        direction = [[1,0],[0,1],[-1,0],[0,-1]] 
        answer = 0    
        count = freshs       
        while queue:
            n = len(queue)
            for i in range(n):
                row,col = queue.popleft()
                for a,b in direction:
                    new_row = row + a
                    new_col = col + b
                    if new_row<0 or new_col < 0 or new_col>=len(grid[0]) or new_row>=len(grid):
                        continue
                    if grid[new_row][new_col] ==1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col))
                        freshs -= 1
            answer += 1            
        if freshs:
            return -1
        if count == freshs:
            return 0
        return answer-1                    
                             
                        
        




        