class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        l=[0]*(len(nums)-1)
        while  len(nums)!=1:
            for i in range(len(nums)-1):
                l[i]=(nums[i]+nums[i+1])%10
            nums=l
            l=[0]*(len(nums)-1)
        return sum (nums)