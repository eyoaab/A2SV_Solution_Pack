class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        voules="aeiou"
        v=0
        _max=0
        for i in range(k):
            if s[i] in voules:
                v+=1
        l=0
        _max=max(_max,v)        
        r=k
        while r<len(s):
                if s[r] in voules:
                    v+=1  
                if s[l] in voules:
                    v-=1
                _max=max(_max,v)   
                l+=1
                r+=1
        return _max    



                 
        