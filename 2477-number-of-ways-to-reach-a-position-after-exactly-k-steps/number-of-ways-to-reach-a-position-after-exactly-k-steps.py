class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        memo = {}

        def dp(pos,k):
            if (pos,k) in memo:
                return memo[(pos,k)]

            if k == 0:
                return pos == endPos 

            result = dp(pos + 1, k - 1) +  dp(pos - 1,k - 1)

            memo[(pos,k)]  = result

            return memo[(pos,k)]
        return dp(startPos,k)  % (10 ** 9  + 7)     