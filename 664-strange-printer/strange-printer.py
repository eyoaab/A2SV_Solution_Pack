class Solution:
    def strangePrinter(self, s: str) -> int:
        @cache
        def f(i, j):
            if i==j: return 1
            if s[i]==s[j]: return f(i, j-1)
            ans=f(i, j-1)+1
            k=i+1
            while k<j-1:
                if s[k]==s[j]:
                    ans=min(ans, f(i, k-1)+f(k, j-1))
                    k+=1
                k+=1
            return ans

        s=[c for c, _ in groupby(s)]
        return f(0, len(s)-1)
        