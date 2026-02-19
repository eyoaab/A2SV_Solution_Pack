class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)
        pre = 0
        i = 0
        
        while i < n:
            cur = 1
            while i < n - 1 and s[i] == s[i + 1]:
                cur += 1
                i += 1
            if pre > 0:
                ans += min(cur,pre)
            pre = cur 
            i += 1

        return ans                   
        