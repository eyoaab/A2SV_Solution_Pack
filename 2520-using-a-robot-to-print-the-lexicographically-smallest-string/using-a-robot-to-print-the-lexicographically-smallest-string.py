class Solution:
    def robotWithString(self, s: str) -> str:
        from collections import Counter

        ans = []
        t = []
        freq = Counter(s)
        sml = 'a'

        for c in s:
            if c == sml:
                ans.append(c)
            else:
                t.append(c)

            freq[c] -= 1
            if freq[c] == 0:
                del freq[c]

            while sml <= 'z' and sml not in freq:
                sml = chr(ord(sml) + 1)

            while t and t[-1] <= sml:
                ans.append(t.pop())

        while t:
            ans.append(t.pop())

        return ''.join(ans)