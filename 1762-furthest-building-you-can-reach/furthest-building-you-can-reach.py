class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        N = len(heights)

        for index in range(N - 1):
            differance = heights[index  + 1] - heights[index]
            
            if differance <= 0:
                continue

            bricks -= differance
            heappush(heap,- differance)

            if bricks < 0:
                if ladders == 0:
                    return index
                ladders -= 1
                new_differance = -heappop(heap) 
                bricks += new_differance
        return  N - 1             

