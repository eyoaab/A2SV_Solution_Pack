class Solution:
    def longestPalindrome(self, s: str) -> int:
        referance=dict(Counter(s).most_common())
        cnt=0
        for i,j in referance.items():
            if j>1:
                if j%2==0:
                    cnt+=j
                else:
                    cnt+=j-1
        for i in  referance.values():
            if i%2!=0:
                return cnt+1
        return cnt                        

            