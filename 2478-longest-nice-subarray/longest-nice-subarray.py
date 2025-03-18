class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans,left,mask = 1 , 0 , 0

        for right,num in enumerate(nums):
            while (mask & num):
                mask ^= nums[left]
                left += 1

            mask |= num
            ans = max(ans,right - left + 1)

        return ans        