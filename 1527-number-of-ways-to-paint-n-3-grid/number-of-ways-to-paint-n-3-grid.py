class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7

        a = [0] * n
        b = [0] * n

        a[0] = 6
        b[0] = 6

        for i in range(1, n):
            a[i] = (2 * a[i-1] + 2 * b[i-1]) % MOD
            b[i] = (2 * a[i-1] + 3 * b[i-1]) % MOD

        return (a[n-1] + b[n-1]) % MOD