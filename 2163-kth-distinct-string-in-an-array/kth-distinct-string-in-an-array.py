class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        store = []

        count = Counter(arr)

        for word in arr:
            if count[word] == 1:
                store.append(word)

        if len(store) < k:
            return '' 

        return store[k - 1]           


        