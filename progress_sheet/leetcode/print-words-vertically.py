class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        leng = 0
        for i in s:
            leng = max(leng, len(i))

        ans = []

        for i in range(leng):
            cur = ''
            for j in range(len(s)):
                if i < len(s[j]):
                    cur += s[j][i]
                else:
                    cur += ' '
            ans.append(cur.rstrip())

        return ans
        