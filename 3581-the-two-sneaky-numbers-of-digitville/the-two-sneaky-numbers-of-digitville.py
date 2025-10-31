class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        store = Counter(nums)
        ans = []

        for num,freq in store.items():
            if freq == 2:
                ans.append(num)

        return ans