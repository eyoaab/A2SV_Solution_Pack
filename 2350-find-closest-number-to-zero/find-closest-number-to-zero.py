class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = nums[0]
        for num in nums:
            if abs(num) < abs(ans):
                ans = num
        if ans < 0 and abs(ans) in nums:
            return abs(ans)

        return ans
            
        