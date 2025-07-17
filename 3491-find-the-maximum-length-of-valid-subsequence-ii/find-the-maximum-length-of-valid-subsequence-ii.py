class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        dp = [[0] * k for _ in range(k)]  
        ans = 0

        for num in nums:
            current = num % k

            for prev in range(k):
                dp[prev][current] = dp[current][prev] + 1

                ans = max(ans, dp[prev][current])

        return ans