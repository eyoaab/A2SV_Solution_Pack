class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        l = []
        d = []
        for i in range(1,n+1):
            if i % m == 0:
                l.append(i)
            else:
                d.append(i)
        
        return sum(d) - sum(l)