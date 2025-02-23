class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        store = defaultdict(int)
        n = len(nums)
        heap = []
        res = [0] * n

        for i, (value, freq) in enumerate(zip(nums, freq)):
            store[value] += freq
            heappush(heap, [-store[value], value])
            while heap and -heap[0][0] != store[heap[0][1]]:
                heappop(heap)
            if heap:
                res[i] = -heap[0][0]
                
        return res         