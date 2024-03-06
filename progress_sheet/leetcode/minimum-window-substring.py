class Solution:

   def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        ans=""
        len_ans=len(s)+1
        l,count=0,0
        tdict=dict(Counter(t))
        need=len(tdict)
        sdict=defaultdict(int)
        for r in range(len(s)):
            if s[r] in tdict:
                sdict[s[r]]+=1
                if sdict[s[r]] == tdict[s[r]]:
                    count += 1
                    while count == need:
                        if r - l + 1 < len_ans:
                            len_ans = r - l + 1
                            ans = s[l:r + 1]

                        if s[l] in sdict:
                            sdict[s[l]] -= 1

                            if sdict[s[l]] < tdict[s[l]]:
                                count -= 1
                        l += 1
        return ans





  