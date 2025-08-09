class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        store = Counter(nums)
        left = {}
        right = {}
        
        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i

        degree = max(store.values())
        ans = len(nums)

        for num in store:
            if store[num] == degree:
                ans = min(ans, right[num] - left[num] + 1)

        return ans