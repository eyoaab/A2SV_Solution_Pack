class Solution:
    def smallestNumber(self, n: int) -> int:
        ans = 1

        while n >  1:
            n //= 2
            ans *= 2
            ans += 1

        return ans