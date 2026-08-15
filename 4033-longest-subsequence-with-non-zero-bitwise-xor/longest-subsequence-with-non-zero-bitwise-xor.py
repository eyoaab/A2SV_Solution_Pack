class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total_xor = 0
        has_non_zero = False
        
        for x in nums:
            total_xor ^= x
            if x != 0:
                has_non_zero = True
                
        if not has_non_zero:
            return 0
        if total_xor != 0:
            return len(nums)
            
        return len(nums) - 1