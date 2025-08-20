class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        n,m = len(matrix),len(matrix[0])

        dp = [[0 for i in range(m + 1)] for j in range(n + 1)]

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = matrix[i][j]

        for i in range(1,n + 1):
            for j in range(1,m + 1):
                if dp[i][j] == 1:
                    dp[i][j] += min(dp[i - 1][j],dp[i][j - 1],dp[i - 1][j - 1])
                    ans +=  dp[i][j]

        return ans                