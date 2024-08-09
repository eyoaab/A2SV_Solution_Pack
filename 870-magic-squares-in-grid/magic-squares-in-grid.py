class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def inbound(row,col):
            return 0 <= row < len(grid) and 0 <= col < len(grid[0])

        def is_valid(row,col):
            temp = set()
            temp.add(grid[row][col])
            directions = [(0,1),(0,-1),(1,0),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]
            _row = defaultdict(int)
            _col = defaultdict(int)
            _row[row] += grid[row][col]
            _col[col] += grid[row][col]


            for delta_x,delta_y in directions:
                new_row = row + delta_x
                new_col = col + delta_y
                if not inbound(new_row,new_col):
                    return False
                value = grid[new_row][new_col]     
                if 1 > value or 9 < value:
                    return False 
                _row[new_row] += value
                _col[new_col] += value    
                temp.add(value)
            print(row,col)
            print('row',_row)
            print(_col)    

            if len(set(_col.values())) > 1 or len(set(_row.values())) > 1:
                return False    
            diagonal_one = grid[row - 1][col - 1] + grid[row + 1][col + 1]
            diagonal_two = grid[row + 1][col - 1] +  grid[row - 1][col + 1] 
            return len(temp) == 9  and diagonal_one == diagonal_two 

        answer = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if  is_valid(row,col):
                    answer += 1

        return answer                         

        