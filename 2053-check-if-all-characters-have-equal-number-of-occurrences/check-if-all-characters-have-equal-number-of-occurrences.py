class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        store = Counter(s)
        return len(set(store.values()))  == 1