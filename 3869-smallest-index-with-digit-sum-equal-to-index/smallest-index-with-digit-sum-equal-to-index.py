class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sumString(num):
            sum_ = 0 
            for s in str(num):
                sum_ += int(s)

            return sum_    

        for i in range(len(nums)):
            if sumString(nums[i]) == i:
                return i

        return -1        
