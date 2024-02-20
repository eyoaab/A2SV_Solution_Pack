class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length=0
        di={}
        l=0
        for r in range (len(s)):
            cha=s[r]
            if(cha in di and l<=di[cha]):
                l=di[cha]+1
            else:
                length=max(length,r-l+1)    
            di[cha]=r
        return  length   



        