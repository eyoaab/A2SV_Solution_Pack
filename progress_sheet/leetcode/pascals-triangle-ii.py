class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex==0:
            return [1]

        answer=[1]
        temp = self.getRow(rowIndex-1)    
        
        for i in  range(1,len(temp)):
            answer.append(temp[i]+temp[i-1])
        answer.append(1)  
        return answer   





        