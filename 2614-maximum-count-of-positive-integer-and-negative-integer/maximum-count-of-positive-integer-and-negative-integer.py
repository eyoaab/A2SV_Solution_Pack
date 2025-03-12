class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        posetive = 0
        negative = 0 

        for num in nums:
            if num < 0:
                negative += 1
            elif num > 0:
                posetive += 1


        return max(posetive,negative)             
        