class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)

        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1

        minq = deque()
        maxq = deque()
        l = 0

        for r, x in enumerate(nums):
            while minq and nums[minq[-1]] >= x:
                minq.pop()
            minq.append(r)

            while maxq and nums[maxq[-1]] <= x:
                maxq.pop()
            maxq.append(r)

            while nums[maxq[0]] - nums[minq[0]] > k:
                if minq[0] == l:
                    minq.popleft()
                if maxq[0] == l:
                    maxq.popleft()
                l += 1

            base = pref[l - 1] if l > 0 else 0
            val = (pref[r] - base) % MOD

            dp[r + 1] = val
            pref[r + 1] = (pref[r] + dp[r + 1]) % MOD

        return dp[n] % MOD