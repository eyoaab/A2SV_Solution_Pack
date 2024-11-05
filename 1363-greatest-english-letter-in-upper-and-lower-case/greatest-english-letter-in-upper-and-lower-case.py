class Solution:
    def greatestLetter(self, s: str) -> str:
        ans = []
        for letter in s:
            if letter.swapcase() in s:
                ans.append(letter.upper())

        return sorted(ans)[-1] if ans else ""        