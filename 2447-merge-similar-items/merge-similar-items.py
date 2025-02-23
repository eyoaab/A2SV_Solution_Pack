class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        store = defaultdict(int)

        for key, val in items1:
            store[key] += val

        for key, val in items2:
            store[key] += val    
            

        return sorted([[key,val] for key,val in store.items()] )