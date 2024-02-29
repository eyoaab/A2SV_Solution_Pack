class Solution:
    def largestOddNumber(self, nums: str) -> str:
        odd="13579"
        for i in range(len(nums)-1,-1,-1):
            if nums[i] in odd:
                return nums[:i+1]
        return ""        
        