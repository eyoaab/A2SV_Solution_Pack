class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        referance={}
        for i in range(len(matrix[0])):
            p=0-i
            referance[p]=matrix[0][i]
        for i in range(len(matrix)):
            referance[i]=matrix[i][0]    

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                k=i-j
                if matrix[i][j] != referance[k]:
                    return False

        return True


        