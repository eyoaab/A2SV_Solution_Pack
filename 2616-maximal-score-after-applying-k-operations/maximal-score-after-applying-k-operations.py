class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap  = []

        for  num in nums:
            heappush(heap,-num)

        score = 0
        while k:
            val = -heappop(heap) 
            score +=  val
            val = ceil(val / 3)

            heappush(heap, -val)
            k -= 1

        return score        