class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        best=right

        while left<=right:
            mid=left+(right-left)//2
            calculated_hour=0
            for pile in piles:
                calculated_hour+=ceil(pile/mid)

            if calculated_hour > h:
                left=mid+1
            else:
                right=mid-1
                best=mid

        return best                