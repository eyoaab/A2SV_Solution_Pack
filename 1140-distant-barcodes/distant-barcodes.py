class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        store = Counter(barcodes)

        heap = []
        for num, count in store.items():
            heappush(heap, (-count, num))

        ans = []
        
        prev_c, prev_n = 0, None

        while heap:
            count, num = heappop(heap)
            ans.append(num)

            if prev_c < 0:
                heappush(heap, (prev_c, prev_n))

            prev_c, prev_n = count + 1, num  

        return ans
