class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        N = len(cost) 
        
        dp = [0] * N 

        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, N):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]  
        
        return min(dp[-1], dp[-2])  