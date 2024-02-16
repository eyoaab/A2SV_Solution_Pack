class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        first=[]
        for i,j in points:
            first.append(i)
        first.sort()    
        max_area=float('-inf')
        for i in range(len(points)-1):
            cur_area=first[i+1]-first[i]
            max_area=max(max_area,cur_area)
        return max_area    


        