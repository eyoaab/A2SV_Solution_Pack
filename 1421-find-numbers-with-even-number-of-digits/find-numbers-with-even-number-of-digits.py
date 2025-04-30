class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ans = 0
        for num in nums:
            ans += len(str(num)) % 2 == 0

        return ans