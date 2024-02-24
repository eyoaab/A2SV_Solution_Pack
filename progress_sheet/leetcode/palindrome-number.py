class Solution:
    def isPalindrome(self, x: int) -> bool:
        def check(p):
            l=0
            r=len(p)-1
            while(l<r):
                if(p[l]!=p[r]):
                    return False
                l+=1
                r-=1 
            return True
        return check(str(x))            
        