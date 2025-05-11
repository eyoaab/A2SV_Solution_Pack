class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        cur = 0

        for num in arr:
            if num % 2 == 1:
                cur += 1
            else:
                cur = 0

            if cur == 3:
                return True

        return False             