class Solution:
    def isGood(self, arr: List[int]) -> bool:
        store = Counter(arr)

        if len(store) != len(arr) - 1:
            return False

        for i in range(1,len(arr) -1):
            if (not i in store.keys()) or  store[i] != 1:
                return False

        if (not len(arr) - 1 in store.keys()) or  store[len(arr) - 1 ] != 2:
            return False

        return True    
        