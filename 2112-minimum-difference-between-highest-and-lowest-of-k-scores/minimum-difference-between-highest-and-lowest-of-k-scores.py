class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)       
        j = k - 1
        i = 0
        mi = abs(nums[k - 1] - nums[0])
        
        while(j < len(nums)):
            d = abs(nums[j] - nums[i])
            mi = min(mi,d)
            j += 1
            i += 1
            
        return mi    