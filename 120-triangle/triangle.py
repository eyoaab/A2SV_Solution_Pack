class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)

        memo = {}
        def dp(index,row):
            if row == N - 1:
                return triangle[row][index]

            if (index,row) in memo:
                return memo[(index,row)]

            follow = dp(index, row + 1)
            not_follow = dp(index + 1 , row + 1)

            memo[(index,row)] = triangle[row][index] + min(follow,not_follow)

            return memo[(index,row)]

        return dp(0,0)            