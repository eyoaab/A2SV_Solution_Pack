class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        size = len(nums)
        dp = [float('-inf')] * size
        curr = 0
        ans = float('-inf')

        for i, n in enumerate(nums):
            curr += n
            if i - k >= 0:
                curr -= nums[i - k]
            if i < k - 1:
                continue
            if i-k >= 0:
                dp[i] = max(dp[i - k] + curr, curr, dp[i])
            else:
                dp[i] = max(dp[i], curr)
            ans = max(ans, dp[i])

        return ans
