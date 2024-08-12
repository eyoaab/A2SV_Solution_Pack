class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        heapify(self.nums)
        self.k = k

        while len(self.nums) > self.k :
            heappop(self.nums)


        
    def add(self, val: int) -> int:
        if len(self.nums)  < self.k:
            heappush(self.nums, val)
        else:
            if self.nums[0] < val:
                heapreplace(self.nums,val)    

        x = self.nums[0]
        return x        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)