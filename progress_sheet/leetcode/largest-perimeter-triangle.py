class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        max_=0
        n=len(nums)-1
        while n>1:     
            if nums[n]<(nums[n-2]+nums[n-1]):       
                max_= max((nums[n-1]+nums[n-2]+nums[n]),max_)
            n-=1    
        return  max_  

        