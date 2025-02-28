class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        cont = dict(Counter(arr))
        return len(set(cont.values())) == len(cont.values())
        