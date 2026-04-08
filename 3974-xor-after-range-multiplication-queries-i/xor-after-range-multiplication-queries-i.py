class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod =  10 ** 9  + 7

        for i, r , k , v in queries:
            for j in range(i,r+1,k):
                nums[j] = (nums[j] * v) % mod

        ans = 0
        for num in nums:
            ans ^= num

        return ans               