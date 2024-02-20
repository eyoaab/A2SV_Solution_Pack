class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        ans=[]
        for i in range(1,len(weights)):
            ans.append(weights[i]+weights[i-1])
        ans.sort()    
        min_=0
        for i in range(k-1):
            min_+=ans[i]
        ans.reverse()    
        max_=0
        for i in range(k-1):
            max_+=ans[i]
            


        return max_-min_     
        