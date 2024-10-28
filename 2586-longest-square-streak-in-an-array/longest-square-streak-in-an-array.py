class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        visited = set()
        ans = 0
        nums.sort()
        store = set(nums)

        for num in nums:
            count = 0
            cur = num

            while cur not in visited and (cur in store):
                visited.add(cur)
                cur *= cur
                count += 1

            ans = max(ans,count) 

        if ans < 2:
            return -1
        return ans          