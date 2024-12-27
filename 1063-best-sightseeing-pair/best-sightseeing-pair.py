class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n = len(values)
        dp, score = 0, 0
        for i, x in enumerate(values):
            score = max(score, dp + x - i)
            dp = max(dp, x + i)
        return score
        