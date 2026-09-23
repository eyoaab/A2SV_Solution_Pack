class Solution:
    def arrangeCoins(self, n: int) -> int:
        def isFull(num):
            val = (num * (num + 1)) // 2
            return val <= n

        left ,right = 1,n
        best = 1
        while left <= right:
            mid = (left + right) // 2
            if isFull(mid):
                best = mid
                left = mid + 1
            else:
                right = mid - 1

        return best                