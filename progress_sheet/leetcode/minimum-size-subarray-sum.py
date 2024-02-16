class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        res=float('inf')
        for j in range(len(nums)):
            total+=nums[j]
            while total>=target:
                res=min(j-l+1,res) 
                total-=nums[l]
                l+=1
        if res==float('inf'):
            return 0
        return res             