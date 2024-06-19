class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        N = len(word1)
        M = len(word2)

        if N == 0:
            return M
        if M == 0:
            return N    

        dp = [[_ for _ in range(M + 1)]]

        for i in range(1,N + 1):
            dp.append([i] + [0 for _ in range(M)])

        print(dp)
        for i in range(1,N + 1):
            for j in range(1,M + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = dp[i - 1][j]
                    delete = dp[i][j - 1]
                    replace =  dp[i - 1][j - 1]

                    dp[i][j] = 1 + min(insert,delete,replace)

        return dp[-1][-1]               



        