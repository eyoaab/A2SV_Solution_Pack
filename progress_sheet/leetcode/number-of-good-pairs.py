class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        referance=dict(Counter(nums))
        ans=0
         
        for key,value in referance.items():
            if value!=1:
                ans+=((value-1)*value)//2

        return ans    
        