class Solution:
    
    def getKth(self, lo: int, hi: int, k: int) -> int:
        memo = {}
        def dp(x:int):
            power = 0
            if x in memo:
                return memo[x]
            if x==1:
                return 0
            if x%2 == 0:
                memo[x]  = 1  + dp(x//2)
            else: 
                memo[x]  = 1 +  dp(3 * x +1)
                
            return memo[x]

        binded = [(x,dp(x)) for x in range(lo, hi + 1)]
        binded.sort(key=lambda x: (x[1], x[0]))
        
        return binded[k - 1][0]
                    