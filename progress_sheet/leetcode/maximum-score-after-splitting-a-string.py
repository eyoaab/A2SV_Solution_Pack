class Solution:
    def maxScore(self, s: str) -> int:
       ma=0
       for i in range(1,len(s)):   
           ma=max(ma,s[:i].count('0')+s[i:].count('1'))
       return ma    
           
        