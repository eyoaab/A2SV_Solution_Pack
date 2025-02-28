class Solution:
    def reverseVowels(self, s: str) -> str:
        voul="aeiouAEIOU"
        ans=""
        v=""
        for i in (s):
            if i in voul:
                v+=i
        c=len(v)-1        
        for i in range(len(s)):
            if s[i] in voul:
                ans+=v[c]
                c-=1
            else:
                ans+=s[i]
        return ans                    


        