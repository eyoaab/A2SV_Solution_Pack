class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        N = len(questions)
        memo = {}
        @cache
        def dp(index):
            if index >= N:
                return 0
            if not index in memo:
                Br = questions[index][-1]
                pt = questions[index][0]

                skip = dp(index + 1)
                solve = pt + dp(index + 1 + Br)
                memo[index] = max(skip,solve)
            return memo[index]

        return dp(0)        