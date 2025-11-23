class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        dp = [0, 0, 0]
        
        for num in nums:
            for cur_max in dp[:]:
                s = cur_max + num
                if s > dp[s % 3]:
                    dp[s % 3] = s

        return dp[0]