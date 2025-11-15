class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        store = [False] * (n + 1)
        store[0] = True
        max_ = max(map(len, wordDict)) 

        for i in range(1, n + 1):
            for j in range(i - 1, max(i - max_ - 1, -1), -1):
                if store[j] and s[j:i] in wordDict:
                    store[i] = True
                    break

        return store[n]