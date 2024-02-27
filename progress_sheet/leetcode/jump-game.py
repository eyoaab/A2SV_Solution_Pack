class Solution:
    def canJump(self, nums: List[int]) -> bool:
        current=nums[0]
        for i in range(1,len(nums)):
            if current==0:
                return False
            current-=1
            current=max(current,nums[i])
        return True        
        