class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        _max=max(candies)
        answer=[False]*len(candies)
        
        for i in range(len(candies)):
            if candies[i]+extraCandies>=_max:
                answer[i]=True

        return answer        
        