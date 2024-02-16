class Solution:
    def sortSentence(self, s: str) -> str:
        ans=['']*len(s.split())
        split=s.split()
        for i in split:
            ans[int(i[-1])-1]=i[:-1]
        return " ".join(ans)     