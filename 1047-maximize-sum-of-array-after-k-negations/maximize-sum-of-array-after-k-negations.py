class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heappush(heap, n)
        while k > 0:
            minimum = heappop(heap)
            heappush(heap,- minimum)
            k -= 1
        return sum(heap)