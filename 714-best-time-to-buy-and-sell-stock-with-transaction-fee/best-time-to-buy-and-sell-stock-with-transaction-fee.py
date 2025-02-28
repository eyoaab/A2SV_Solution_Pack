class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        N = len(prices)
        dp = {}

        def dfs(index,buying):

            if index >= N:
                return 0

            if (index,buying) in dp:
                return dp[(index,buying)]

            if buying:

                buy = -prices[index] + dfs(index + 1,not buying)
                not_buy =  dfs(index + 1,buying)

                dp[(index,buying)]  = max(buy,not_buy)

            else:

                sell = prices[index] - fee  + dfs(index + 1,not buying)
                not_sell  = dfs(index + 1,buying)

                dp[(index,buying)] = max(sell,not_sell) 

            return dp[(index,buying)]

        return dfs(0,True)                   