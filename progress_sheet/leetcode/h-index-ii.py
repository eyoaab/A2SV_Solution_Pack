class Solution:
    def hIndex(self, citations: List[int]) -> int:
        

        left,right = 0,len(citations)-1
        citations.reverse()

        while left <= right:
            mid = left + (right - left)//2
            
            if citations[mid] >= mid+1:
                left = mid+1      
            else:
                 right = mid - 1
                

        return left            

    
        