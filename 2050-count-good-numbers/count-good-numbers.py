class Solution:
    def countGoodNumbers(self, n: int) -> int:

        mod=(10**9)+7
      
        return (pow(5,ceil(n/2),mod) * pow(4,n//2,mod))% mod     