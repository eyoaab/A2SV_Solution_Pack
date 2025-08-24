class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = 0
        ones = 0
        ans = 0
        left = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero += 1
                if zero > 1:
                    while nums[left] != 0:
                        ones -= 1
                        left += 1
                    left += 1    
                    zero -= 1
            else:
                ones += 1
                ans = max(ans,ones) 

        if ans == len(nums):
            return ans - 1 

        return ans     
                

        