class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        current=capacity
        answer=0

        for i in range(len(plants)):
            if i!=len(plants)-1:
                current-=plants[i]
                answer+=1
                if plants[i+1]>current:
                    answer+=(i+1)*2
                    current=capacity
                
            else:
                answer+=1

        return answer        
                            
        