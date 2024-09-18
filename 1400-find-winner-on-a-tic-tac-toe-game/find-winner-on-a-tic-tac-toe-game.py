class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        n = len(moves)
        matrix = [[0] * 3 for _ in range(3)]
        
        def isvalid(directions):
            hash_map = Counter(directions)
            del hash_map[0]
            for key, count in hash_map.items():
                if count == 3:
                    return key
                    
        for i in range(n):
            if i % 2 == 0:
                row, col = moves[i]
                matrix[row][col] = 'A'
            else:
                row, col = moves[i]
                matrix[row][col] = 'B'


        for row in matrix:
            row_map = Counter(row)
            del row_map[0]
            for key, count in row_map.items():
                if count == 3:
                    return key

        ########### Column #######################

        for j in range(len(matrix)):
            columns = [row[j] for row in matrix]
            col_map = Counter(columns)
            del col_map[0]
            for key, count in col_map.items():
                if count == 3:
                    return key

        ########### diagonal #######################
        
        diagonal,anti_diagonal  = [], []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i - j == 0:
                    diagonal.append(matrix[i][j])
                if i + j == 2:
                    anti_diagonal.append(matrix[i][j])

        diagonal_map = Counter(diagonal)
        del diagonal_map[0]
        for key, count in diagonal_map.items():
            if count == 3:
                return key

        anti_diagonal_map = Counter(anti_diagonal)
        del anti_diagonal_map[0]
        for key, count in anti_diagonal_map.items():
            if count == 3:
                return key

        
        return "Draw" if len(moves) == 9 else'Pending'