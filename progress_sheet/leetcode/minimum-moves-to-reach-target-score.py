class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        n=target
        mc=maxDoubles
        result=0
        while n>1:
            if mc>0:
                if n%2!=0:
                    result+=1
                    n-=1
                else:
                    n=n//2
                    result+=1
                    mc-=1
            else:
                return result+n-1
                
        return result                    

        