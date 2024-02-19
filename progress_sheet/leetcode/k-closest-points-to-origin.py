class Solution:
    def helper(self,arr):
        return sqrt(arr[0]**2+(arr[1]**2))
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        referance=[]
        for point in points:
            referance.append(self.helper(point))
        new_list=[]    
        for i in range(len(points)): 
            temp=points[i]
            temp.append(referance[i])
            new_list.append(temp)   
        new_list.sort(key=lambda x:(x[-1],x[1],x[0])) 
        answer=[]
        for i in range(k):
            answer.append(new_list[i][:2])
        return answer      