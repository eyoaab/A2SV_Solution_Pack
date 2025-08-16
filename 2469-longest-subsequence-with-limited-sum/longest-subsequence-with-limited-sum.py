
class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:

        size = len(nums)
        nums.sort()
        prefix = list(accumulate(nums))
        ans = []
        for query in queries:
            index = bisect_right(prefix, query)
            ans.append(index)

        return ans




        