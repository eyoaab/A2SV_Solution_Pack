class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []

        for gift in gifts:
            heappush(heap,-gift)


        while k and heap:   
            val = -heappop(heap)
            val = int(sqrt(val))

            if val > 0:
                heappush(heap,-val)

            k -= 1    

        return -sum(heap)     
