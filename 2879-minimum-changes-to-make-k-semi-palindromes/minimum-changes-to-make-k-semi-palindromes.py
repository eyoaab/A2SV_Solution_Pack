class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)

        cost = [[0] * n for _ in range(n)]

        for length in range(2, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                best = length

                for divisor in range(1, length // 2 + 1):
                    if length % divisor != 0:
                        continue

                    changes = 0

                    for residue in range(divisor):
                        low = left + residue
                        high = left + residue + ((length - 1 - residue) // divisor) * divisor

                        while low < high:
                            if s[low] != s[high]:
                                changes += 1
                            low += divisor
                            high -= divisor

                        if changes >= best:
                            break

                    best = min(best, changes)

                    if best == 0:
                        break

                cost[left][right] = best


        INF = 10 ** 9
        dp = [[INF] * (n + 1) for _ in range(k + 1)]
        dp[0][0] = 0

        for parts in range(1, k + 1):
            for end in range(2 * parts, n - 2 * (k - parts) + 1):
                best = INF

                for start in range(2 * (parts - 1), end - 1):
                    if dp[parts - 1][start] == INF:
                        continue
                    best = min(best, dp[parts - 1][start] + cost[start][end - 1])

                dp[parts][end] = best

        return dp[k][n]