class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
        
        N = len(nums)
        
        average = (nums[0] + nums[-1] )/ 2
        
        left = 0
        right = N - 1
        
        while left < right:
           
            N -= 2  
            
            average = min(average,(nums[left] + nums[right])/ 2)
            
            left += 1
            right -= 1
        
        return average
