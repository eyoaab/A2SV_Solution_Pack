class Solution:
    def helper(self, a, b, dp):
        if a <= 0 and b > 0:
            return 1.0
        if a == 0 and b == 0:
            return 0.5
        if a > 0 and b <= 0:
            return 0.0
        if a <= 0 and b <= 0:
            return 0.5
        if dp[a][b] != -1:
            return dp[a][b]

        x = 0.25 * self.helper(a - 100, b, dp)
        y = 0.25 * self.helper(a - 75, b - 25, dp)
        z = 0.25 * self.helper(a - 50, b - 50, dp)
        w = 0.25 * self.helper(a - 25, b - 75, dp)

        dp[a][b] = x + y + z + w
        return dp[a][b]

    def soupServings(self, n):
        if n > 4800:
            return 1.0
        dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
        return self.helper(n, n, dp)