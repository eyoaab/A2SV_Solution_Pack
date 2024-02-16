class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        r=len(people)-1
        l=0
        boat=0
        while(l<=r):
            if people[l]+people[r]<=limit:
                
                r-=1
                l+=1
            else:
                r-=1
            boat+=1 
        return boat       



        