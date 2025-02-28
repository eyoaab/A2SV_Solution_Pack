class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        if maze[entrance[0]][entrance[1]] == "+":
            return -1

        ans = float('inf')
        roww,coll = len(maze),len(maze[0]) 
        def isBound(r,c): 
            return (0 <= r < roww) and (0 <= c < coll)  

        def isBorder(r,c): 
            # print(r,c)/
            return (r == 0 or r == roww - 1 ) or (c == 0 or c == coll - 1 )
        
        visited = set()
        directions = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = deque()
        queue.append([entrance[0],entrance[1],0])


        while queue:

            row,col,count = queue.popleft()
            # print(row,col,count)
            if isBorder(row, col) and [row, col] != entrance:
                return count

            visited.add((row,col)) 
            for dx,dy in directions:
                if isBound(dx + row,dy + col) and  maze[dx + row][dy + col] == "." and (dx + row,dy + col) not in visited :
                    queue.append([dx + row,dy + col,count + 1])
                    visited.add((dx + row,dy + col) )
                    
        return -1 
