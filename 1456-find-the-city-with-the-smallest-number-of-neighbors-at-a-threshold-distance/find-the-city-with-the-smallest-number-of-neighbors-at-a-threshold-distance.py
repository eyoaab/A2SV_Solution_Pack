class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        matrix = [[float('inf') for i in range(n)] for j in range(n)]

        for diagonal in range(n):
            matrix[diagonal][diagonal]=  0
        
        for edge in edges:
            start,end,distance =  edge
            matrix[start][end] = distance
            matrix[end][start] = distance


        for pivot in range(n):

            for row in range(n):
                for col in range(n):
                   matrix[row][col] = min(matrix[row][col],matrix[pivot][col] + matrix[row][pivot])


        answer = [0 for i in range(n)]

        # print(matrix)

        for node in range(n):
            row = matrix[node]

            for x in row:
                if x <= distanceThreshold:
                    answer[node] += 1

        for i in range(n-1,-1,-1):
            if answer[i] == min(answer):
                return i

        return 0                     

           

             
