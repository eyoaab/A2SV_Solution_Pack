class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        heap = []

        for num in set(nums):
            heappush(heap,-num)

        if len(heap) < 3:
            return - heappop(heap)

        heappop(heap)
        heappop(heap)

        return -heappop(heap)        