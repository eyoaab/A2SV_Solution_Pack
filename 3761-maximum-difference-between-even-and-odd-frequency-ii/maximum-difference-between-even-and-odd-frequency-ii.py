class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def getStatus(cnta,cntb):
            return ((cnta&1)<<1)|(cntb&1)
        n=len(s)
        ans=float("-inf")
        for a in "01234":
            for b in "01234":
                if a==b:
                    continue
                best=[float("inf")]*4
                cnta=cntb=0
                preva=prevb=0
                left=-1
                for right in range(n):
                    cnta+=s[right]==a
                    cntb+=s[right]==b
                    while right-left>=k and cntb-prevb>=2:
                        leftstatus=getStatus(preva,prevb)
                        best[leftstatus]=min(best[leftstatus],preva-prevb)
                        left+=1
                        preva+=s[left]==a
                        prevb+=s[left]==b
                    rightstatus=getStatus(cnta,cntb)
                    if best[rightstatus^0b10]!=float("inf"):
                        ans=max(ans,cnta-cntb-best[rightstatus^0b10])
        return ans if ans!=float("-inf") else -1