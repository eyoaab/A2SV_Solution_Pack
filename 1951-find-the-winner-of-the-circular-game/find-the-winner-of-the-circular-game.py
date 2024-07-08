class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        l=[i for i in range(1,n+1)]
        start=0
        r=0
        while(len(l)!=1):
            r=(start + k-1)%len(l)
            l.pop(r)
            start=r
                
        return l[0]