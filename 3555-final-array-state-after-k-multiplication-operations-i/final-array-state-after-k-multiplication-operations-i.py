class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = []

        for i,num in enumerate(nums):
            heappush(heap,[num,i])

        while k:
            val,index = heappop(heap)
            val *= multiplier
            heappush(heap,[val,index])
             
            k -= 1

        while heap:
            val,index = heappop(heap)
            nums[index] = val

        return nums    

                


