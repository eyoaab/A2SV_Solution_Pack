class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        referance=defaultdict(list)
        row=len(matrix)
        column=len(matrix[0])

        for i in range(row):
            for j in range(column):
                referance[i+j].append(matrix[i][j])

        answer=[]
        for key , value in referance.items():
            if key%2==0:
                answer.extend(value[::-1])
            else:
                answer.extend(value)
        return answer