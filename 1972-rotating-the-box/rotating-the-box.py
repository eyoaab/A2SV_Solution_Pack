class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for row in box:
            emptyIndex = len(row) - 1  
            for j in range(len(row) - 1, -1, -1):
                if row[j] == '#':
                    row[j], row[emptyIndex] = row[emptyIndex],row[j]
                    emptyIndex -= 1
                elif row[j] == '*': 
                    emptyIndex = j - 1

     
        return [[box[i][j] for i in range(len(box) - 1, -1, -1)] for j in range(len(box[0]))]
