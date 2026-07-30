class Solution:
    def minimumPushes(self, word: str) -> int:

        n = len(word)

        cost = 0

        x = n // 8

        for i in range(1, x + 1):
            cost += 8 * i

        y = n % 8

        cost += y * (x + 1)

        return cost