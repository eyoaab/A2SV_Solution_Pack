class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        ans = 0
        for s in set(word):
            ans += s.swapcase() in word

        return ans // 2    