class Solution(object):
    def numTilings(self, n):
        dp, MOD = [0] * (max(4, n + 1)), 10**9 + 7
        for i, num in enumerate([1, 1, 2, 5]):
            dp[i] = num
        for i in range(4, n + 1):
            dp[i] = (2 * dp[i - 1] + dp[i - 3]) % MOD
        return dp[n]