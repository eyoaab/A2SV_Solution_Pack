class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        updated = []
        for row in nums:
            updated.append(sorted(row))

        n = len(nums[0])

        column = {i:0 for i in range(n)} 

        for  row in range(len(nums)):
            for i in range(n):
                val = updated[row][i]  
                column[i]  = max(column[i],val)

        return sum(column.values())        
        