class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        N = len(matrix)

        row = defaultdict(set)
        col = defaultdict(set)

        for i  in range(N):
            for j in range(N):
                if matrix[i][j] in row[i] or  matrix[i][j] in col[j]:
                    return  False

                row[i].add(matrix[i][j])  
                col[j].add(matrix[i][j]) 

        return True        

