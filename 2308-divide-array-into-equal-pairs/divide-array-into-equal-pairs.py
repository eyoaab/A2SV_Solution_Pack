class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        store = Counter(nums)
        for i,j in store.items():
            if j % 2 != 0:
                return False

        return True        