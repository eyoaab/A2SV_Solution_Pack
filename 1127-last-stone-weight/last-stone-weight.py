class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapify(stones)

        while len(stones) > 1:
            num1 = -heappop(stones)
            num2 = -heappop(stones)

            _min = min(num1,num2)

            num1 -= _min
            num2 -= _min

            if num1:
                heappush(stones, - num1)
            if num2:
                heappush(stones, - num2)  

        if stones:
            return -stones[0]

        return 0              

