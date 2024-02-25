class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        while True:
            if n%2==0:
                return n
            n=n*2    
        