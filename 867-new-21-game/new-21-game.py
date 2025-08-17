#copy
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k == 0 or n >= k - 1 + maxPts:
            return 1.0

        dp = [0.0] * maxPts
        dp[0] = 1.0

        sum_ = 1.0
        result = 0.0

        for i in range(1, n + 1):
            prob = sum_ / maxPts

            if i < k:
                sum_ += prob
            else:
                result += prob

            if i >= maxPts:
                sum_ -= dp[i % maxPts]

            dp[i % maxPts] = prob

        return result