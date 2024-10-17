class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        heap = []
        if len(nums) < 3:
            return -1
        for num in nums:
            heappush(heap, num)

        heappop(heap)

        if heap:
            return heappop(heap)

        return -1        