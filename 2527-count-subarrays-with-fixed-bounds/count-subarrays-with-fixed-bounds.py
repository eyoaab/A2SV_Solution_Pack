class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        minI = -1
        maxI = -1
        left = -1
        right = 0
        count = 0
        
        while right < len(nums):
            if nums[right] < minK or nums[right] > maxK:
                minI = right
                maxI = right
                left = right
            
            minI = right if nums[right] == minK else minI
            maxI = right if nums[right] == maxK else maxI
            
            count += min(minI, maxI) - left
            right += 1
        
        return count