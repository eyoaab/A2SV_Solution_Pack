class Solution:
    def help(self,s,l,r):
        if l>=r:
            return
        s[l],s[r]=s[r],s[l]
        self.help(s,l+1,r-1)
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l=-1
        r=len(s)
        self.help(s,l+1,r-1)    
        
         

      
        
        