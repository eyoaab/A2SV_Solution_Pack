class Solution:
    def minSumOfLengths(self, A: List[int], k: int) -> int:
        n = len(A)
        res, tot, i = n + 1, 0, 0

        # dp[j] = min len of a valid subarray ending before index j
        dp = [n] * (n + 1)

        for j in range(n):
            tot += A[j]

            # Move → while (sum < k) --> expand the current subarray.
            # Move ↓ while (sum > k) --> shrink the current subarray.
            while tot > k:
                tot -= A[i]
                i += 1
                
            dp[j + 1] = dp[j]

            if tot == k:
                Len = j - i + 1

                # dp[i] is the min len in the box before i,
                # so it cannot overlap.
                res = min(res, Len + dp[i])
                dp[j + 1] = min(dp[j], Len)
                
        return -1 if res == n + 1 else res