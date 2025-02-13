class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        count = 0
        for num in nums:
            heappush(heap,num)

        while heap and heap[0] < k and len(heap) > 1:
            num1,num2 = heappop(heap),heappop(heap)
            num3 = min(num1,num2) * 2 + max(num1,num2) 
            count += 1
            heappush(heap,num3)

        return count     