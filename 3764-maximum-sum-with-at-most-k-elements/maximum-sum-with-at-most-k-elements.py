class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        heap = []

        for index,row in enumerate(grid):
            minHeap = []
            for num in row:
                heappush(minHeap, -num)

            count = 0
            while count < limits[index] and minHeap:
                heappush(heap,heappop(minHeap)) 
                count += 1

        ans = 0

        while k and heap:
            k -= 1
            ans += -heappop(heap)

        return ans         
        