class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        ans = 0

        for word in words:
            ans += word.startswith(pref)

        return ans    