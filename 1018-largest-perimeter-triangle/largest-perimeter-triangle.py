class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        ans = 0
        n = len(nums) - 1
        
        while n > 1:     
            if nums[n] < (nums[n - 2] + nums[n - 1]):       
                ans = max((nums[n - 1] + nums[n - 2] + nums[n]),ans)
            n -= 1    
        
        return ans  

        