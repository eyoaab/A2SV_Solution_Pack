class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while(l<r):
            current=min(height[l],height[r])*(r-l)
            maxarea=max(maxarea,current)
            if(height[l]<=height[r]):
                l+=1
            elif(height[r]<height[l]):
                r-=1  
        return  maxarea         
            
