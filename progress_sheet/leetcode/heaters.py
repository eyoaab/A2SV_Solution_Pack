class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        def check(rad):
            i,j = 0,0
          
            while i<len(houses) and j<len(heaters):
                if abs(heaters[j]-houses[i]) <= rad:
                    i+=1
                else:
                    j+=1

            if j>=len(heaters) and i <len(houses):
                return False
            return True

        houses.sort()
        heaters.sort()
        left,right = 0,max(houses[-1],heaters[-1])
        radius=0

        while left <= right:
            mid=left + (right-left)//2
            
            if check(mid):
                radius=mid
                right=mid-1
            else:
                left=mid+1 

        return radius           
         

        