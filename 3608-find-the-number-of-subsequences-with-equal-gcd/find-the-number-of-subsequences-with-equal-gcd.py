class Solution:
    def subsequencePairCount(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [[[-1] * 201 for _ in range(201)] for _ in range(n + 1)]

        def solve(idx, gcd1, gcd2):
            if idx == n:
                return 1 if gcd1 != 0 and gcd1 == gcd2 else 0

            if dp[idx][gcd1][gcd2] != -1:
                return dp[idx][gcd1][gcd2]

            ans = 0

            ans += solve(idx + 1, gcd1, gcd2)

            ans += solve(idx + 1, gcd(gcd1, nums[idx]), gcd2)

            ans += solve(idx + 1, gcd1, gcd(gcd2, nums[idx]))

            dp[idx][gcd1][gcd2] = ans % MOD
            return dp[idx][gcd1][gcd2]

        return solve(0, 0, 0)