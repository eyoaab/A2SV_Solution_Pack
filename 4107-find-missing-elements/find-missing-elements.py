class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        min_, max_ = min(nums),max(nums)
        ans = []
        nums = set(nums)

        for num in range(min_,max_):
            if num not in nums:
                ans.append(num)

        return ans