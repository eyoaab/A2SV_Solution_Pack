class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        left_best = [[0] * n for _ in range(n)]

        right_best = [[0] * n for _ in range(n)]

        left_ptr = [0] * n

        right_ptr = list(range(n))

        for i in range(n):
            left_best[i][i] = stoneValue[i]
            right_best[i][i] = stoneValue[i]

            left_ptr[i] = i - 1

            right_ptr[i] = i

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[r + 1] - prefix[l]

                while left_ptr[l] + 1 <= r - 1:
                    k = left_ptr[l] + 1
                    left_sum = prefix[k + 1] - prefix[l]

                    if 2 * left_sum > total:
                        break

                    left_ptr[l] += 1

                while right_ptr[l] <= r - 1:
                    k = right_ptr[l]
                    left_sum = prefix[k + 1] - prefix[l]

                    if 2 * left_sum >= total:
                        break

                    right_ptr[l] += 1

                best = 0

                if left_ptr[l] >= l:
                    best = left_best[l][left_ptr[l]]

                if right_ptr[l] <= r - 1:
                    best = max(
                        best,
                        right_best[right_ptr[l] + 1][r]
                    )

                dp[l][r] = best

                left_best[l][r] = max(
                    left_best[l][r - 1],
                    dp[l][r] + total
                )

                right_best[l][r] = max(
                    right_best[l + 1][r],
                    dp[l][r] + total
                )

        return dp[0][n - 1]