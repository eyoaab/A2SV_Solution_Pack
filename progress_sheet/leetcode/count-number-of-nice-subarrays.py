class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
     
        right ,left = 0,0
        ans = 0 
        odd = 0
        ans = 0
        cur = 0
        for right in range(len(nums)):
            
            if nums[right]%2 == 1:
                odd += 1
                cur = 0
                
            while odd == k:
                if nums[left]%2 == 1:
                    odd -= 1
                cur += 1
                left += 1
                
            ans += cur
            
        return ans