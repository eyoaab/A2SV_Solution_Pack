class Solution:
    def findLHS(self, nums: List[int]) -> int:
        store = Counter(nums)

        ans = 0
        for num in nums:
            if num + 1 in store:
                ans = max(ans,store[num] + store[num + 1])


        return ans