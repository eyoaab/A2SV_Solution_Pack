class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        rep = 1
        powers = []
        
        while n > 0:
            if n % 2 == 1:
                powers.append(rep)

            n //= 2    
            rep *= 2

        ans = []
        for left,right in  queries:
            cur = 1
            for i in range(left,right + 1):
                cur *= powers[i]

            ans.append(cur % mod)    



        return ans

