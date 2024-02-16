class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        ls=0
        for i in range(len(nums)):
            if(sum-nums[i]==ls):
                return i
            ls+=nums[i]
            sum-=nums[i]  
        return -1      