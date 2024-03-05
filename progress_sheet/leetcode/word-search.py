class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_len = len(board)
        col_len = len(board[0])
        visited=set()

        def helper(row,col,index):
            if index>=len(word):
                return True
            if  (row,col) in visited:
                return False  
            if row < 0 or col<0:
                return False
            if row >= row_len or col>=col_len:
                return False
            if board[row][col] != word[index]:
                return False
            visited.add((row,col))
            path1=helper(row+1,col,index+1) 
            path2=helper(row-1,col,index+1) 
            path3=helper(row,col+1,index+1) 
            path4=helper(row,col-1,index+1) 
            ans=path1 or path2 or path3 or path4
            visited.remove((row,col))

            return ans


        for i in range(row_len):
            for j in range(col_len):
                if helper(i,j,0):
                    return True

        return False            

            
           

