class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        keep = ""
        if n % 2 == 1:
            keep = s[n // 2]

        chars = s[:n // 2]

        half = "".join(sorted(chars))

        res = half + keep + half[::-1]

        return res