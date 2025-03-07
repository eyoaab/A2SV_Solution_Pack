class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        isPrime = [True for i in range(right + 1)]

        isPrime[0] = isPrime[1] = False

        for i in range(2,int(right ** 0.5) + 1):
            if isPrime[i]:
                for j in range(i * i,right + 1, i):
                    isPrime[j] = False

        primes = [index for index,val in enumerate(isPrime) if val and index >= left]
        if(len(primes) < 2):
            return [-1,-1]
        ans = []
        previousGap = float('inf')    

        for i in range(1,len(primes)):
            gap = primes[i] - primes[i - 1]
            if gap <  previousGap:
                ans = [primes[i-1], primes[i]]  
                previousGap = gap

        return ans if ans else [-1,-1]      

        