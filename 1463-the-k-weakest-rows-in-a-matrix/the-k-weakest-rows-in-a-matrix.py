class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        store = []

        for index,row in enumerate(mat):
            store.append([sum(row),index])

        store.sort()
        print(store)

        return [ index for num,index in store[:k]]