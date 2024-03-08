class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        answer=[]
        for i,j in firstList:
            for x,y in secondList:
                if i<=x and j<=y and x<=j:
                    answer.append([x,j])  
                elif i<=x and y<=j:
                    answer.append([x,y])
                elif x<=i and i<=y and y<=j:
                    answer.append([i,y])
                elif x<=i and j<=y:
                    answer.append([i,j]) 
        return answer                          

        

      
       
                 
