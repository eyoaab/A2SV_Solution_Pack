class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        p=0
        if len(s)>len(t):
            return False
        if  len(s)==0:
            return True    

        for i in range(len(t)):
            if(p<len(s)):
                if(s[p]==t[i]):
                    p+=1
        return p==len(s)        


              

          
        