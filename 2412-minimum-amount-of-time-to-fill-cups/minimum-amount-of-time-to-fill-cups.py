class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []

        for num in amount:
            if num:
                heappush(heap,-num)

        steps = 0

        while heap:
            if len(heap) < 2:
                steps += -1 * heap[0]
                break
            num1,num2 = -heappop(heap),-heappop(heap)

            num1 -= 1
            num2 -= 1

            if num1:
                heappush(heap,-num1) 
            if num2:
                heappush(heap,-num2) 

            steps += 1        



        return steps        