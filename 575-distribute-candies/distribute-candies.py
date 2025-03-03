class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        avaliable = len(candyType) // 2
        return min(len(set(candyType)),avaliable)