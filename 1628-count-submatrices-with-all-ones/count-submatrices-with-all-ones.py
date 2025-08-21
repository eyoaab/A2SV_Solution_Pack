class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        dp = [[0] * m for _ in range(n)]
        
        for j in range(m):
            for i in range(n):
                if mat[i][j] == 0:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i - 1][j] + 1 if i > 0 else 1

        ans = 0
        for i in range(n):
            stack = []
            sum_ = 0
            for j in range(m):
                cnt = 1
                while stack and stack[-1][0] >= dp[i][j]:
                    h, c = stack.pop()
                    sum_ -= h * c
                    cnt += c
                sum_ += dp[i][j] * cnt
                stack.append((dp[i][j], cnt))
                ans += sum_
                
        return ans
