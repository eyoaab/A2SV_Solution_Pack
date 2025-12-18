class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)
        ans = 0

        for i in range(k, n):
            ans += prices[i] * strategy[i]

        cur = ans

        for i in range(k):
            ans += prices[i] * strategy[i]

            if i >= k // 2:
                cur += prices[i]

        ans = max(ans, cur)

        for i in range(k, n):
            cur += prices[i - k] * strategy[i - k]

            cur -= prices[i - k // 2]

            cur -= prices[i] * strategy[i]
            cur += prices[i]

            ans = max(ans, cur)

        return ans