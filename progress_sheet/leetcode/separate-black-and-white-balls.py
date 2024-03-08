class Solution:
    def minimumSteps(self, s: str) -> int:
        ans=0
        zeros=0
        for i in range(len(s)):
            if s[i]=='0':
                ans+=i-zeros
                zeros+=1
        return ans        