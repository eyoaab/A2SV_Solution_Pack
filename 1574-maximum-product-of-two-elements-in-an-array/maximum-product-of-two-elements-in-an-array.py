class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [num - 1 for num in nums]
        ans = float('-inf')

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                ans = max(ans,nums[i] * nums[j])

        return ans        