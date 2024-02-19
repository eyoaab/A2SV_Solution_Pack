class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        max_amount=0
        bob=0
        alice=len(piles)-1
        while bob+1<alice:
            max_amount+=piles[alice-1]
            alice-=2
            bob+=1
        return max_amount    

        