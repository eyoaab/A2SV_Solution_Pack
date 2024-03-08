class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        prefix=[0]*10000
        left=1000
        right=0

        for trip in trips:
            person,start,end=trip
            prefix[start]+=person
            prefix[end]-=person
            left=min(left,start)
            right=max(right,end)
            
        answer=0
        for pre in range(left,right+1):
            answer+=prefix[pre]
            if answer>capacity:
                return False

        return True        



            

        