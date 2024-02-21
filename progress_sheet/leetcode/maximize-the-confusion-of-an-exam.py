class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        ref={
            'T':0,
            'F':0
        }
        r=1
        l=0
        n=len(s)
        _max=0
        ref[s[0]]+=1
        while r<n:
            ref[s[r]]+=1
            while min(ref.values())>k:
                ref[s[l]]-=1
                l+=1
            _max=max(r-l+1,_max) 
            r+=1
        return max(_max,n-l)       


                