class Solution:
    def numWaterBottles(self, n: int, k: int) -> int:
        def exchange(n, k):
            if n < k:
                return 0
            n0 , r = divmod(n, k)
            return n0 + exchange(n0 + r, k)


        return n + exchange(n, k)
        