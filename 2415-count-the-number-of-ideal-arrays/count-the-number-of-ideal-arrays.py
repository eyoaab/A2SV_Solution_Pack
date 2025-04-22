class Solution:
    MOD = 1000000007
    fact_memo = [0] * 100000
    dp = [[0] * 15 for _ in range(100000)]
    def fast_power(self, x, base, m) -> int:
        output = 1
        while base:
            if base & 1: output = (output * x) % m
            x = (x * x) % m
            base >>= 1
        return output

    def fact(self, n) -> int:
        if not n: return 1
        if self.fact_memo[n]: return self.fact_memo[n]
        self.fact_memo[n] = (n * self.fact(n - 1)) % self.MOD
        return self.fact_memo[n]

    def mod_inv(self, x, y) -> int:
        return (((self.fact(x) * self.fast_power(self.fact(y), self.MOD - 2, self.MOD)) % self.MOD) * self.fast_power(self.fact(x - y), self.MOD - 2, self.MOD)) % self.MOD

    def idealArrays(self, n, maxValue) -> int:
        for num in range(1, maxValue + 1):
            for d in range(1, min(n, 14) + 1):
                self.dp[num][d] = 0
        for num in range(1, maxValue + 1):
            
            self.dp[num][1] = 1
            div = 2
            while div * num <= maxValue:
                for k in range(1, min(n, 14)):
                    self.dp[num * div][k + 1] += self.dp[num][k]
                div += 1

        output = 0

        for num in range(1, maxValue + 1):
            for d in range(1, min(n, 14) + 1):
                output = (output + self.mod_inv(n - 1, n - d) * self.dp[num][d]) % self.MOD

        return output